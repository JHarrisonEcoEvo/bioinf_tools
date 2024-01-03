# Simple bioinformatic tools 
Routine tools and a template for future projects.

The plan is to add custom scripts for various tasks here. This will update an old repo I had that was similar in purpose but is now deprecated.

## Tools by type and their usage:
### Basic string tools
- count_nuc - counts the number of times each nucleotide occurs in a string. (count_nuc -s STRING)
- rev_comp - returns the reverse complement of a string. (rev_comp -i STRING)
- gc_content - returns the GC content of a string.  (function in seq_tools)
- sliding_window - returns GC content of string over sliding window. (function in seq_tools)

### Conversion and IO tools
- parquet_converter - convert a parquet file to a csv. (-input, -i, path)

# Installation
After cloning this repo, navigate into it and type:
```pip install ./```
