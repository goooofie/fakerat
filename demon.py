import ctypes

MessageBoxA = ctypes.windll.user32.MessageBoxA
NULL = 0
MB_OK = 0

MessageBoxA(NULL, ctypes.c_char_p(b"RATTED!!!"), ctypes.c_char_p(b"Win.32.Sys"), MB_OK)



var = ctypes.c_bool(True)