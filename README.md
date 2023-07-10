# Running the files here


Added a C++ file (`demo1.cpp`), a Python script (`demo2.py`) and a Jupyter notebook (`demo3.ipynb`) demonstrating GHZ state construction for 30 qubits using single-GPU acceleration. 

For the C++ file and the Python script, you'll need the flag `--target nvidia` to access GPU acceleration. Dropping this flag would make the program run with the default CPU target, causing it to slow down significantly.

The instructions to run these files are given below (also inside each file).

<ol>
<li> To run the C++ file </li>

 ` nvq++ demo1.cpp --target nvidia `




<li>To run the Python script</li> 

`python3 demo2.py --target nvidia`
  



<li> The target is set internally in the Jupyter notebook (demo3.ipynb). Run as you'd normally run a notebook. </li>
