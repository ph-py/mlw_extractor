import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def extract_mlw(input_path):
  if not os.path.exists(input_path):
    print(f"file not found: {input_path}")
    return

  with open(input_path, 'rb') as f:
    mlw_data = f.read()
    root_idx = mlw_data.find(b'Root\x00')

    if root_idx == -1:
      print("root marker not found")
      return

    filename_start = root_idx + 5
    null_idx = mlw_data.find(b'\x00', filename_start)
  
    if null_idx == -1:
      print("end of the filename not found")
      return

    offset = null_idx + 13
    key = bytes.fromhex("d27e154628ae2ba6ab4b9775165ff737")
    iv = mlw_data[offset:offset+12]
    ct = mlw_data[offset+16:-16]
    auth_tag = mlw_data[-16:]
    print(f"payload offset: 0x{offset:X}")

  try:
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, auth_tag), backend=default_backend())
    decryptor = cipher.decryptor()
    dec = decryptor.update(ct) + decryptor.finalize()
    output_path = os.path.splitext(input_path)[0] + ".mp4"

    with open(output_path, 'wb') as f:
      f.write(dec)
      print(f"video extracted to: {output_path}")
  
  except Exception as e:
    print(f"failed: {e}")

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("usage: python mlw_extractor.py <file.mlw>")
  else:
    extract_mlw(sys.argv[1])
