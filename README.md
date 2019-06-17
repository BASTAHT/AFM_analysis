A way to quickly analyse/enhance multiple AFM graphs using gwyddion functions. The results are saved as .jpg and .gwy files to allow for further (manual) processing.
The function used are:
- set color range to automatic
- level plane
- align rows (default polynomial)
- remove scars (multiple times)
- fix zero
  
A root dir is selected and all AFM files in all subdirs will be analysed. Files with an already corresponding .gwy file will be ignored.
The code only works using __Python 2.7 32-bit__ and __Gwyddion 32-bit__.
