# Decompile with IDA

#/*Decompile Code*/
'''
__int64 __fastcall sub_140001000(__int64 a1)
{
  int i; // [rsp+0h] [rbp-18h]

  for ( i = 0; (unsigned __int64)i < 0x18; ++i )
  {
    if ( byte_140003000[i] != (i ^ *(unsigned __int8 *)(a1 + i)) + 2 * i )
      return 0i64;
  }
  return 1i64;
}

//byte_140003000()
49h, 60h, 67h, 74h, 63h, 67h, 42h, 66h, 80h, 78h, 2 dup(69h)
7Bh, 99h, 6Dh, 88h, 68h, 94h, 9Fh, 8Dh, 4Dh, 0A5h, 9Dh
45h, 8 dup(0)

//Make up
[0x49, 0x60, 0x67, 0x74, 0x63, 0x67, 0x42, 0x66, 0x80, 0x78, 0x69, 0x69, 0x7B, 0x99, 0x6D, 0x88, 0x68, 0x94, 0x9F, 0x8D, 0x4D, 0xA5, 0x9D, 0x45, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

//Hex to Dec
[73, 96, 103, 116, 99, 103, 66, 102, 128, 120, 105, 105, 123, 153, 109, 136, 104, 148, 159, 141, 77, 165, 157, 69, 0, 0, 0, 0, 0, 0, 0, 0]
'''

#Inverse Operation.py
dec = [73, 96, 103, 116, 99, 103, 66, 102, 128, 120, 105, 105, 123, 153, 109, 136, 104, 148, 159, 141, 77, 165, 157, 69]

flag=[]

for i in range(0, 24):
    inverse = ((dec[i] - (2 * i)) ^ i)
    char = chr(inverse)
    flag.append(char)

print(flag, end="")


'''
=========================================================
DH{I_am_X0_xo_Xor_eXcit1ng}
=========================================================
'''