#!/bin/bash

echo -e "Arguments:
[0] - Used by Bash (script filename)
[1] - Base directory
[2] - Filename type (maximum two values)
[3] - Ignored files or folders (optional; use "\""./<directory_name>"\"")
"

echo "Changed files:"


# Separate $2 value (filename types) if it has a comma
if [[ "$2" == *","* ]];
then
string="$2"

str_value=${string#*,}
str_value2=${string%%,*}
else
str_value="$2"
str_value2="$2"
fi

IFS=$'\n'; set -f
for fname in $(find $1 -type f -name "*$str_value2" -or -name "*$str_value")
do
    ignored_files="$(echo "$3" | tr "," "\n")"

    str="${fname}"
    value=${str%/*} # If the base directory is `.`, check in all directories for the ignored filenames

    for files in $ignored_files
    do
        if [ "${fname}" == "$value/$files" ] || [ "$value" == "$files" ];
        then
            continue 2
        fi
    done

    #echo ${fname}
    new_fname=$(echo "${fname}" | tr ' ' '_')
    #echo "      ${new_fname}"
    new_fname=$(echo "${new_fname}" | tr '[:upper:]' '[:lower:]')
    #echo "      ${new_fname}"
    new_fname=$(echo "${new_fname}" | tr '-' '_')
    #echo "      ${new_fname}"
    if [ "${fname}" != "${new_fname}" ]
    then
        echo "      ${fname} --> ${new_fname}"
    fi
done
unset IFS; set +f
