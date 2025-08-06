Raspberry Pi Pico-based Robot Cars programmed in MicroPython.

For the mecanum wheel car with the IR remote, here is what you need to do:

add a file called `main.py` to the pi pico
paste the code in `mecanum_ir.py`

make a folder on the pico called `ir_rx`

make files in that folder, called:
`__init__.py` (that is two underscores either side)
`nec_8.py`
`print_error.py`

copy the code for those files, from the subdirectory `ir_rx` in this repository,
https://github.com/peterhinch/micropython_ir
