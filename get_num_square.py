import os

num = os.environ.get("INPUT_NUM")
if num:
    try:
        num = int(num)
    expect Exception:
        exit('ERROR: the INPUT-NUM provided ("{}")is npt ')
else:
    num = 1
    
print(f"::set-output name=num_squared::{num ** 2}")
