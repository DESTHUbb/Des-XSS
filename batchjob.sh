#########################################################################
# File Name: batchjob.sh
# Author: longwenzhang
#Created Time:2019.12.31
#########################################################################
#!/bin/bash

#Scan big data in batch to avoid highly use of cpu&memory.
python start.py --file url --filter
line=`cat url.filtered|wc -l`
if [ $line -lt 10000 ]
then
	python start.py --file url.filtered
else
	start=1
	count=10000
	end=10000
	while [ $end -lt $line ]
	do
		sed -n "$start,$end p" url.filtered>url.slice
		# delete traffic files after scanning.
		python start.py --file url.slice --clear
		let start+=count
		let end+=count
	done
	sed -n "$start,$line p" url.filtered>url.slice
	# delete traffic files after scanning.
	python start.py --file url.slice --clear
	cat urls.slice
fi

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#########################################################################
# File Name: batchjob.sh
# Author: DESTHUbb
#Created Time:2019.12.31
#########################################################################


#!/bin/bash
# Script to download images in batches

# Run the Python script to download the images
python3 download_images.py --source "https://example.com/images" --output "output_directory" --batch_size 100

# Check the number of files downloaded
num_files=$(ls -1 output_directory | wc -l)

# If less than 100 images were downloaded, exit the script
if [ "$num_files" -lt 100 ]; then
    echo "Less than 100 images were downloaded, exiting."
    exit 1
fi

# Split the downloaded images into batches of 50 files
split -l 50 output_directory/files.txt output_directory/files_

# Process each batch of files
for file in output_directory/files_*
do
    # Download the images in the current batch
    xargs -n 1 curl -O < "$file"
    
    # Delete the batch file
    rm "$file"
done

echo "All images have been downloaded and processed."
Este script comienza ejecutando un programa Python llamado "download_images.py" que descarga imágenes desde una URL proporcionada en lotes de 100 imágenes. Luego, verifica cuántos archivos se han descargado y, si son menos de 100, sale del script.

Si se han descargado al menos 100 imágenes, el script divide los archivos descargados en lotes de 50 archivos utilizando el comando "split". Luego, procesa cada lote de archivos descargados utilizando el comando "xargs" para descargar las imágenes restantes en cada lote. Finalmente, elimina los archivos de lote y muestra un mensaje indicando que todas las imágenes han sido descargadas y procesadas.
