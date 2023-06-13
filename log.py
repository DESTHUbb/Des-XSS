#!/usr/bin/env python

"""
Output
"""

import logging
import re
import sys

class ColorizingStreamHandler(logging.StreamHandler):
    # color names to indices
    color_map = {
        'black': 0,
        'red': 1,
        'green': 2,
        'yellow': 3,
        'blue': 4,
        'magenta': 5,
        'cyan': 6,
        'white': 7,
    }

    # levels to (background, foreground, bold/intense)
    level_map = {
        logging.DEBUG: (None, 'blue', False),
        logging.INFO: (None, 'green', False),
        logging.WARNING: (None, 'yellow', False),
        logging.ERROR: (None, 'red', False),
        logging.CRITICAL: ('red', 'white', False)
    }
    csi = '\x1b['
    reset = '\x1b[0m'
    bold = "\x1b[1m"
    disable_coloring = False

    @property
    def is_tty(self):
        isatty = getattr(self.stream, 'isatty', None)
        return isatty and isatty() and not self.disable_coloring

    def emit(self, record):
        try:
            message = self.format(record)
            stream = self.stream

            if not self.is_tty:
                if message and message[0] == "\r":
                    message = message[1:]
                stream.write(message)
            else:
                self.output_colorized(message)
            stream.write(getattr(self, 'terminator', '\n'))

            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except IOError:
            pass
        except:
            self.handleError(record)

    def output_colorized(self, message):
        self.stream.write(message)

    def _reset(self, message):
        if not message.endswith(self.reset):
            reset = self.reset
        elif self.bold in message:  # bold
            reset = self.reset + self.bold
        else:
            reset = self.reset

        return reset

    def colorize(self, message, levelno):
        if levelno in self.level_map and self.is_tty:
            bg, fg, bold = self.level_map[levelno]
            params = []

            if bg in self.color_map:
                params.append(str(self.color_map[bg] + 40))

            if fg in self.color_map:
                params.append(str(self.color_map[fg] + 30))

            if bold:
                params.append('1')

            if params and message:
                if message.lstrip() != message:
                    prefix = re.search(r"\s+", message).group(0)
                    message = message[len(prefix):]
                else:
                    prefix = ""

                message = "%s%s" % (prefix, ''.join((self.csi, ';'.join(params),
                                   'm', message, self.reset)))

        return message

    def format(self, record):
        message = logging.StreamHandler.format(self, record)
        return self.colorize(message, record.levelno)

LOGGER = logging.getLogger("")
LOGGER_HANDLER = None
try:
    class _ColorizingStreamHandler(ColorizingStreamHandler):
        def colorize(self, message, levelno):
            if levelno in self.level_map and self.is_tty:
                bg, fg, bold = self.level_map[levelno]
                params = []

                if bg in self.color_map:
                    params.append(str(self.color_map[bg] + 40))

                if fg in self.color_map:
                    params.append(str(self.color_map[fg] + 30))

                if bold:
                    params.append('1')

                if params and message:
                    match = re.search(r"\A(\s+)", message)
                    prefix = match.group(1) if match else ""
                    message = message[len(prefix):]

                    match = re.search(r"\[([A-Z ]+)\]", message)  # log level
                    if match:
                        level = match.group(1)
                        if message.startswith(self.bold):
                            message = message.replace(self.bold, "")
                            reset = self.reset + self.bold
                            params.append('1')
                        else:
                            reset = self.reset
                        message = message.replace(level, ''.join((self.csi, ';'.join(params), 'm', level, reset)), 1)

                        match = re.search(r"\A\s*\[([\d:]+)\]", message)  # time
                        if match:
                            time = match.group(1)
                            message = message.replace(time, ''.join((self.csi, str(self.color_map["cyan"] + 30), 'm', time, self._reset(message))), 1)

                        match = re.search(r"\[(#\d+)\]", message)  # counter
                        if match:
                            counter = match.group(1)
                            message = message.replace(counter, ''.join((self.csi, str(self.color_map["yellow"] + 30), 'm', counter, self._reset(message))), 1)

                        if level != "PAYLOAD":
                            if any(_ in message for _ in ("parsed DBMS error message",)):
                                match = re.search(r": '(.+)'", message)
                                if match:
                                    string = match.group(1)
                                    message = message.replace("'%s'" % string, "'%s'" % ''.join((self.csi, str(self.color_map["white"] + 30), 'm', string, self._reset(message))), 1)
                            else:
                                match = re.search(r"\bresumed: '(.+\.\.\.)", message)
                                if match:
                                    string = match.group(1)
                                    message = message.replace("'%s" % string, "'%s" % ''.join((self.csi, str(self.color_map["white"] + 30), 'm', string, self._reset(message))), 1)
                                else:
                                    match = re.search(r" \('(.+)'\)\Z", message) or re.search(r"output: '(.+)'\Z", message)
                                    if match:
                                        string = match.group(1)
                                        message = message.replace("'%s'" % string, "'%s'" % ''.join((self.csi, str(self.color_map["white"] + 30), 'm', string, self._reset(message))), 1)
                                    else:
                                        for match in re.finditer(r"[^\w]'([^']+)'", message):  # single-quoted
                                            string = match.group(1)
                                            message = message.replace("'%s'" % string, "'%s'" % ''.join((self.csi, str(self.color_map["white"] + 30), 'm', string, self._reset(message))), 1)
                    else:
                        message = ''.join((self.csi, ';'.join(params), 'm', message, self.reset))

                    if prefix:
                        message = "%s%s" % (prefix, message)

                    message = message.replace("%s]" % self.bold, "]%s" % self.bold)  # dirty patch

            return message

    LOGGER_HANDLER = _ColorizingStreamHandler(sys.stdout)
except ImportError:
    LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

FORMATTER = logging.Formatter("\r[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S")

LOGGER_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(LOGGER_HANDLER)
LOGGER.setLevel(logging.INFO)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

DESCRIPICION:
    
Este script es un controlador de registros que proporciona colorización de salida y formato personalizado para los mensajes de registro. 
Utiliza la biblioteca de registro de Python y agrega una capa adicional para dar formato y color a los mensajes de registro.

La parte del código que se encarga de la colorización depende del terminal que se esté utilizando, y utiliza códigos ANSI para establecer el color de la salida. 
La función emit es la encargada de escribir los mensajes de registro y la función format define el formato que se va a utilizar para los mensajes de registro.

La clase ColorizingStreamHandler hereda de logging.StreamHandler y sobrescribe los métodos emit y format para agregar la colorización. 
También define dos diccionarios, color_map y level_map, que mapean los nombres de colores y los niveles de registro a los códigos ANSI correspondientes.

La clase _ColorizingStreamHandler es una subclase de ColorizingStreamHandler que agrega aún más funcionalidad para la colorización de mensajes.

En resumen, este script es un controlador de registro especializado que proporciona una salida de registro más legible y atractiva visualmente al agregar color y formato a los mensajes de registro.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

MEJORA Y ACTUALIZACION:
    
import logging
import re
import sys
from typing import Any, Dict, Optional, Tuple


class ColorizingStreamHandler(logging.StreamHandler):
    color_map: Dict[str, int] = {
        'black': 0,
        'red': 1,
        'green': 2,
        'yellow': 3,
        'blue': 4,
        'magenta': 5,
        'cyan': 6,
        'white': 7,
    }

    level_map: Dict[int, Tuple[Optional[str], str, bool]] = {
        logging.DEBUG: (None, 'blue', False),
        logging.INFO: (None, 'green', False),
        logging.WARNING: (None, 'yellow', False),
        logging.ERROR: (None, 'red', False),
        logging.CRITICAL: ('red', 'white', False)
    }

    csi: str = '\x1b['
    reset: str = '\x1b[0m'
    bold: str = "\x1b[1m"
    disable_coloring: bool = False

    @property
    def is_tty(self) -> bool:
        isatty = getattr(self.stream, 'isatty', None)
        return isatty and isatty() and not self.disable_coloring

    def emit(self, record: logging.LogRecord) -> None:
        try:
            message = self.format(record)
            stream = self.stream

            if not self.is_tty:
                if message and message[0] == "\r":
                    message = message[1:]
                stream.write(message)
            else:
                self.output_colorized(message)
            stream.write(getattr(self, 'terminator', '\n'))

            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except IOError:
            pass
        except:
            self.handleError(record)

    def output_colorized(self, message: str) -> None:
        self.stream.write(message)

    def _reset(self, message: str) -> str:
        if not messagecontinuing from the previous answer...

    def _reset(self, message: str) -> str:
        if not message:
            return message
        return f"{self.csi}0m{message}{self.reset}"

    def _colorize(self, message: str, fg: Optional[str] = None, bg: Optional[str] = None, bold: bool = False) -> str:
        if not message:
            return message

        fg_code = self.color_map.get(fg, None)
        bg_code = self.color_map.get(bg, None)

        if fg_code is None and bg_code is None and not bold:
            return message

        codes = []
        if fg_code is not None:
            codes.append(f"{self.csi}{30 + fg_code}m")
        if bg_code is not None:
            codes.append(f"{self.csi}{40 + bg_code}m")
        if bold:
            codes.append(self.bold)

        codes_str = "".join(codes)
        reset_str = self._reset("")
        return f"{codes_str}{message}{reset_str}"

    def format(self, record: logging.LogRecord) -> str:
        level = record.levelno
        if level not in self.level_map:
            level_name = str(level)
            level_fg, level_bg, level_bold = None, None, False
        else:
            level_name, level_fg, level_bold = self.level_map[level]
            level_bg = 'black' if level_fg in ('white', 'yellow') else None

        level_name = level_name or logging.getLevelName(level)
        level_name = level_name.capitalize()

        name = record.name
        if name.startswith("root."):
            name = name[5:]

        message = record.getMessage()
        message = re.sub(r"\x1b\[\d+(;\d+)*m", "", message)
        message = message.rstrip()

        prefix = f"[{name}:{record.lineno}] [{level_name}] "
        prefix = self._colorize(prefix, fg=level_fg, bg=level_bg, bold=level_bold)

        message = self._colorize(message, fg='white')
        return f"{prefix}{message}"

    def __init__(self, stream: Optional[Any] = None) -> None:
        super().__init__(stream)
        self.setLevel(logging.DEBUG)


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    handler = ColorizingStreamHandler(sys.stdout)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    
 Agregar documentación a las clases y métodos: Es importante que el código esté bien documentado para que sea fácil de entender y mantener. 
 Agregar documentación a las clases y métodos ayudará a los desarrolladores que trabajen en el código en el futuro.

Utilizar nombres de variables más descriptivos: Los nombres de las variables deben ser descriptivos y permitir entender fácilmente lo que representa. 
Por ejemplo, en el código se utiliza bg, fg, bold para representar el color de fondo, el color del texto y si es negrita o no, respectivamente. 
Sería mejor utilizar nombres más descriptivos como background_color, foreground_color y is_bold.

Agregar comentarios: Además de la documentación en las clases y métodos, es una buena práctica agregar comentarios para explicar partes específicas del código que puedan ser difíciles de entender.

Utilizar f-strings para la interpolación de cadenas: En lugar de concatenar cadenas utilizando el operador +, es recomendable utilizar f-strings (disponibles a partir de Python 3.6) para hacer la interpolación de variables en las cadenas. 
Esto hace que el código sea más legible y reduce la posibilidad de errores.

Utilizar logging.getLogger(__name__) en lugar de logging.getLogger(""): En lugar de pasar una cadena vacía como argumento a getLogger(), es preferible utilizar __name__ como argumento.
Esto hace que el nombre del logger sea el nombre del módulo en el que se está ejecutando el código, lo que hace que sea más fácil identificar de dónde provienen los mensajes de registro.

Utilizar super() para llamar a los métodos de la superclase: En lugar de llamar a los métodos de la superclase utilizando logging.StreamHandler.method(self, args), es preferible utilizar super().method(args), lo que hace que el código sea más legible y menos propenso a errores.

Evitar la duplicación de código: En el código hay algunas partes que se repiten en diferentes métodos. Es recomendable refactorizar el código para evitar la duplicación de código.

Utilizar typing para especificar tipos de datos: Es recomendable utilizar typing para especificar los tipos de datos que se utilizan como argumentos y valores de retorno en los métodos.













