#########################################################################
# File Name: batchjob.sh
# Author: DESTHUbb
#Created Time:2023.06.12
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
This script starts by running a Python program called "download_images.py" that downloads images from a given URL in batches of 100 images. Then it checks how many files have been downloaded and if less than 100 it exits the script.
If at least 100 images have been downloaded, the script splits the downloaded files into batches of 50 files using the "split" command. It then processes each batch of downloaded files using the "xargs" command to download the remaining images in each batch. Finally, it deletes the batch files and displays a message indicating that all the images have been downloaded and processed.
