# I. Forensics

![image](https://user-images.githubusercontent.com/91616280/227745147-6b7eedb4-7c71-493b-b47e-a222f0ce7159.png)


## Solution

- Chúng ta sẽ có 1 file rar khi tải về máy.
- Mở file rar và xem qua thì thấy đây là 1 folder chứa nhiều folder con hơn nữa và bên trong mỗi folder sẽ có nhiều folder tiếp tục mở thì trong mỗi folder sẽ có 10 file txt.
- Để tìm ra flag bài này cũng có rất nhiều tool hỗ trợ nhưng tôi sẽ dùng luôn chức năng tìm kiếm của winrar bằng công cụ Find trong Winrar.

![image](https://user-images.githubusercontent.com/91616280/227745287-ba9a6e14-480d-4b08-8c04-53f084b990f9.png)

## Flag

- Chúng ta sẽ có flag: `ATTT{https://www.youtube.com/watch?v=4qNALNWoGmI}`


# II. Crypto

## 1. Crypto1

![image](https://user-images.githubusercontent.com/91616280/227745381-3c091ce8-8795-4164-9ef7-090e51cf8342.png)

## Solution

- Cùng xem qua nội dung của 2 file enc.cpp và file bases.txt nhận thấy file enc.cpp có sử dụng 3 bases cơ sở đó là octal, dec và hex.

```
#include <iostream>
#include <string>
using namespace std;

#define EL printf("\n")

string flag = "ATTT{fake_flag}";

void bases(string &s) {
    for (int i = 0; i < s.size(); i += 4)
        printf("%o %u %x %u ", (unsigned char) s[i], (unsigned char) s[i + 1], (unsigned char) s[i + 2], (unsigned char) s[i + 3]);
    EL;
}

int main() {
    freopen("bases.txt", "w", stdout);
    bases(flag);

    return 0;
}


```
- Sau khi mở file base.txt nó sẽ ghi vào lần lượt theo thứ tự của chuỗi `ATTT{fake_flag}` theo dạng octal, dec, hex, hex. khi chạy đoạn encypt này ta nhận được chuỗi sau :
```
101 84 54 84 173 102 61 107 145 95 66 108 141 103 7d 0 
```

- Từ đó có thể nhận thấy được các giá trị của file bases.txt mà để bài cho sẽ được ép kiểu sang các dạng khác lần lượt như trên:
```
101 84 54 84 173 77 65 111 167 95 6d 101 157 119 5f 109 145 111 77 95 155 101 6f 119 137 116 72 97 137 108 61 105 137 116 61 109 137 116 72 105 137 116 6f 105 137 100 61 121 175

```

- Ta sẽ viết 1 script python để tìm ra flag như sau:
```
s = ["101","84","0x54","84","173","77","0x65","111","167","95","0x6d","101","157","119","0x5f","109","145","111","0x77","95","155","101","0x6f","119","137","116","0x72","97","137","108","0x61","105","137","116","0x61","109","137","116","0x72","105","137","116","0x6f","105","137","100","0x61","121","175"]
result = ""
for i in range(0, min(len(s), len(s)//4*4), 4):
    octV = int(s[i], 8)
    decV1 = int(s[i+1], 10)
    hexV = int(s[i+2], 16)
    decV2 = int(s[i+3], 10)
    asciiV = chr(octV) + chr(decV1) + chr(hexV) + chr(decV2)
    result += asciiV

result += chr(int(s[len(s)-1], 8))
print(result)

```
## FLag

```
 Halston    D:\svatttptit2023\crypto1  ﮫ 1.586s   5:37 AM  
 ⚡ndinh ❯❯ python -u "d:\svatttptit2023\crypto1\crypto1.py"
ATTT{Meow_meow_meow_meow_tra_lai_tam_tri_toi_day}
```

## 2. Crypto2

![image](https://user-images.githubusercontent.com/91616280/227745776-20b3359d-0b81-4ca7-bc5c-d4afb42e8e34.png)

## Solution

- Tôi đã tham khảo và viết ra 1 tool để tính tần suất xuất hiện (phá mã hóa thay thế).
```
import pandas as pd

a = []
b = []
f = open("d:/svatttptit2023/crypto2/x.txt", "r")
for line in f:
    line = line.strip() # remove leading/trailing whitespace
    if line not in a:
        a.append(line)
        b.append(1)
    else:
        b[a.index(line)] += 1

sum = 0
for i in b:
    sum += i
print(sum)

d = ["R", "T", "E", "A", "O", "L", "N", "S", "I", "C", "U", "D", "P", "M", "H", "G", "B", "F", "Y", "W", "K", "V", "X", "Z", "J", "Q", "_", " ", "-", "{", "}", "."]  # Add 4 more elements to match the length of a, b, and c

c = []
for i in b:
    c.append(i / sum * 100)

df = pd.DataFrame({'Ciphertext' : a, 'Appear' : b, 'Frequency': c})
df = df.sort_values('Appear', ascending=[False])
df['Alphabet'] = d
print(df)
```

- Khi chạy đoạn code tính tần suất ta thu được số lần xuất hiện của từng chuỗi như sau:
```
⚡ndinh ❯❯ python -u "d:\svatttptit2023\crypto2\test.py"
1080
                            Ciphertext  Appear  Frequency Alphabet                                                                                                                                    
3     821b5788942bc3c602d59d08841f7639     216  20.000000        R                                                                                                                                    
2     79baa5dd638b9dd358e0ebd73a2f04d5     112  10.370370        T                                                                                                                                    
8     e170db7f88034def96d72730bb471a49      94   8.703704        E                                                                                                                                    
12    c7a8b2b718344a552973e2194f54316e      69   6.388889        A                                                                                                                                    
7     8135c0c9ab41c1e2feb5dc7c7725084c      66   6.111111        O                                                                                                                                    
10    92de53110cc6b7997b23db17334349b0      55   5.092593        L                                                                                                                                    
11    2d83f1f43737775272277cf51a241f9b      54   5.000000        N                                                                                                 
5     39fed56a74ee6bdeedae3327a4ef3a87      52   4.814815        S
4     fcd6a5a5f5a0a5b0eea7645e96aa73f3      48   4.444444        I
20    85500929da2c7c6ad31eb86612888a62      38   3.518519        C
19    7888df48adf1316bf7d4b22408cc8738      38   3.518519        U
1     873192d689147d39d203e2123d9760e4      34   3.148148        D
14    93c532c22b931d43985806e7f367138c      23   2.129630        P
16    e7a3af5b7959ea248ae9d3e422bf87f1      22   2.037037        M
0     8e5fa4a16eb745968a04f328ca859ca8      19   1.759259        H
13    53978afa51e371cdbd245fb4034df6b5      19   1.759259        G
21    543899ba352fc27c310dc5dfcda5a3d3      18   1.666667        B
18    60f98c48275cd54521bc27cc24c74ca2      16   1.481481        F
9     cf683f3b1a04ce72b0116dcd0058bf43      15   1.388889        Y
23    dd343191f74151b93aafebdb3b19dc73      13   1.203704        W
22    710fd3add964a6ae4274af49a7b0a48d      12   1.111111        K
15    2de4cd0d9a12844ac673e9d2d446d1cf      12   1.111111        V
24    e2be8d5d04a4e97e3a74546dfc4ea104      11   1.018519        X
6     aaac38f5e1d306c5d66e78f386719dc9       7   0.648148        Z
17    21aec3f0635563dc13c9989166be4403       4   0.370370        J
27    2745714dc397f17b1258c3523c9d4469       3   0.277778        Q
29    7334d85f5c104c2b0f8318d371f94819       3   0.277778        _
25    bbf1b91698f6c5bc0c1a9652016d56ff       2   0.185185
26    0da357f52f343040cbb1c198e16d1c9d       2   0.185185        -
28    110da0235675bc52e3d3a20b65ee2d69       1   0.092593        {
30  a143b07765f0c492802cccbe10c2ad2d {       1   0.092593        }
31  eef25089a95b61ed453fc34e13bae049 }       1   0.092593        .
```

- Dùng công cụ visual studio code chúng ta sẽ thấy rõ được những đoạn giống nhau theo form flag là `ATTT{flag}` vì vậy ta sẽ tìm chữ T và cụm `{}` do chỉ xuất hiện 1 lần nên ta sẽ có được khoảng flag chính xác.

![image](https://user-images.githubusercontent.com/91616280/227746260-43cbcffd-6ab4-4c16-941d-749369209e73.png)

- vậy đây chính là khoảng flag mà chúng ta cần tìm, công việc còn lại khá đơn giản chỉ cần tìm đúng chuỗi và chuyển các kí tự vào ghép lại thành 1 chuỗi đúng nghĩa.
- Khi làm đến cuối ta thấy số sẽ bị trống ở chữ cái cuối cùng. Lúc này ta cần phải đoán được từ cuối sao cho flag có nghĩa. 

```
c7a8b2b718344a552973e2194f54316e A
79baa5dd638b9dd358e0ebd73a2f04d5 T
79baa5dd638b9dd358e0ebd73a2f04d5 T
79baa5dd638b9dd358e0ebd73a2f04d5 T
110da0235675bc52e3d3a20b65ee2d69 {
92de53110cc6b7997b23db17334349b0 
8135c0c9ab41c1e2feb5dc7c7725084c O
79baa5dd638b9dd358e0ebd73a2f04d5 T
7334d85f5c104c2b0f8318d371f94819 _
c7a8b2b718344a552973e2194f54316e A
7334d85f5c104c2b0f8318d371f94819 _
39fed56a74ee6bdeedae3327a4ef3a87 S
873192d689147d39d203e2123d9760e4 U
8e5fa4a16eb745968a04f328ca859ca8 B
39fed56a74ee6bdeedae3327a4ef3a87 S
79baa5dd638b9dd358e0ebd73a2f04d5 T
fcd6a5a5f5a0a5b0eea7645e96aa73f3 I
79baa5dd638b9dd358e0ebd73a2f04d5 T
873192d689147d39d203e2123d9760e4 
79baa5dd638b9dd358e0ebd73a2f04d5 T
fcd6a5a5f5a0a5b0eea7645e96aa73f3 I
8135c0c9ab41c1e2feb5dc7c7725084c O
92de53110cc6b7997b23db17334349b0 
7334d85f5c104c2b0f8318d371f94819 _
710fd3add964a6ae4274af49a7b0a48d 
fcd6a5a5f5a0a5b0eea7645e96aa73f3 I
aaac38f5e1d306c5d66e78f386719dc9 
2d83f1f43737775272277cf51a241f9b 
e170db7f88034def96d72730bb471a49 E
e7a3af5b7959ea248ae9d3e422bf87f1 
a143b07765f0c492802cccbe10c2ad2d }
```
- Ta cùng lật lại đề bài `But today is not the day for subtitution cipher. Today I'm using AES encryption to protect my secret. Can you break it?`
- Với dữ kiện trên ta có thể đoán luôn flag:
```
c7a8b2b718344a552973e2194f54316e A
79baa5dd638b9dd358e0ebd73a2f04d5 T
79baa5dd638b9dd358e0ebd73a2f04d5 T
79baa5dd638b9dd358e0ebd73a2f04d5 T
110da0235675bc52e3d3a20b65ee2d69 {
92de53110cc6b7997b23db17334349b0 N
8135c0c9ab41c1e2feb5dc7c7725084c O
79baa5dd638b9dd358e0ebd73a2f04d5 T
7334d85f5c104c2b0f8318d371f94819 _
c7a8b2b718344a552973e2194f54316e A
7334d85f5c104c2b0f8318d371f94819 _
39fed56a74ee6bdeedae3327a4ef3a87 S
873192d689147d39d203e2123d9760e4 U
8e5fa4a16eb745968a04f328ca859ca8 B
39fed56a74ee6bdeedae3327a4ef3a87 S
79baa5dd638b9dd358e0ebd73a2f04d5 T
fcd6a5a5f5a0a5b0eea7645e96aa73f3 I
79baa5dd638b9dd358e0ebd73a2f04d5 T
873192d689147d39d203e2123d9760e4 U
79baa5dd638b9dd358e0ebd73a2f04d5 T
fcd6a5a5f5a0a5b0eea7645e96aa73f3 I
8135c0c9ab41c1e2feb5dc7c7725084c O
92de53110cc6b7997b23db17334349b0 N
7334d85f5c104c2b0f8318d371f94819 _
710fd3add964a6ae4274af49a7b0a48d C
fcd6a5a5f5a0a5b0eea7645e96aa73f3 I
aaac38f5e1d306c5d66e78f386719dc9 P
2d83f1f43737775272277cf51a241f9b H
e170db7f88034def96d72730bb471a49 E
e7a3af5b7959ea248ae9d3e422bf87f1 R
a143b07765f0c492802cccbe10c2ad2d }
```
## Flag
- Ta thu về được flag: `ATTT{NOT_A_SUBSTITUTION_CIPHER}`

# III. Re

## 1. Re03

![image](https://user-images.githubusercontent.com/91616280/227746543-40ec4b83-462d-4183-84c3-3a8bac53dd57.png)

## Solution

- Đây là file ComplimentaryChallenge.exe: PE32 executable (console) Intel 80386, for MS Windows.

- Sử dụng công cụ IDA để xem code của nó.
- Đây là đoạn code từ hàm main.
```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  FILE *v3; // eax
  FILE *v5; // eax
  FILE *v6; // eax
  DWORD Mode; // [esp+18h] [ebp-20h] BYREF
  char Str[4]; // [esp+1Ch] [ebp-1Ch] BYREF
  int v9; // [esp+20h] [ebp-18h]
  int v10; // [esp+24h] [ebp-14h]
  int v11; // [esp+28h] [ebp-10h]
  HANDLE hConsoleHandle; // [esp+2Ch] [ebp-Ch]

  __main();
  *(_DWORD *)Str = 523448849;
  v9 = 406598155;
  v10 = 557725189;
  v11 = 3741480;
  xor_strings(Str, "ISPw");
  hConsoleHandle = GetStdHandle(0xFFFFFFF5);
  if ( hConsoleHandle == (HANDLE)-1 )
  {
    v3 = ___acrt_iob_func(2u);
    fwrite("Failed to get console handle\n", 1u, 0x1Du, v3);
    return 1;
  }
  else if ( GetConsoleMode(hConsoleHandle, &Mode) )
  {
    Mode |= 4u;
    if ( SetConsoleMode(hConsoleHandle, Mode) )
    {
      printf("Flag: ATTT{%s}\x1B[2K\x1B[1GWhat are you waiting for?", Str);
      return 0;
    }
    else
    {
      v6 = ___acrt_iob_func(2u);
      fwrite("Failed to set console mode\n", 1u, 0x1Bu, v6);
      return 1;
    }
  }
  else
  {
    v5 = ___acrt_iob_func(2u);
    fwrite("Failed to get console mode\n", 1u, 0x1Bu, v5);
    return 1;
  }
}
```

- Có thể thấy đáng chú ý nhất trong hàm main này là khi mà chương trình gọi hàm `xor_string()` để xor chuỗi str với `ISPw`

```
unsigned int __cdecl xor_strings(char *Str, char *a2)
{
  unsigned int result; // eax
  size_t v3; // [esp+14h] [ebp-14h]
  size_t v4; // [esp+18h] [ebp-10h]
  unsigned int i; // [esp+1Ch] [ebp-Ch]

  v4 = strlen(Str);
  v3 = strlen(a2);
  for ( i = 0; ; ++i )
  {
    result = i;
    if ( i >= v4 )
      break;
    Str[i] ^= a2[i % v3];
  }
  return result;
}
```

- Ta sử dụng công cụ debug trên ida để xem nội dung chuối str đặt `br*` tại `ret` ta có thể thấy được chuỗi cuối cùng sau khi chương trình thực hiện phép xor khi xem trên stack của nó.
![image](https://user-images.githubusercontent.com/91616280/227747463-9f95c8aa-7473-42eb-9149-5ca3deb85aec.png)

```
Stack[00004EC0]:0061FEAC db  58h ; X
Stack[00004EC0]:0061FEAD db  61h ; a
Stack[00004EC0]:0061FEAE db  63h ; c
Stack[00004EC0]:0061FEAF db  68h ; h
Stack[00004EC0]:0061FEB0 db  42h ; B
Stack[00004EC0]:0061FEB1 db  61h ; a
Stack[00004EC0]:0061FEB2 db  6Ch ; l
Stack[00004EC0]:0061FEB3 db  6Fh ; o
Stack[00004EC0]:0061FEB4 db  4Ch ; L
Stack[00004EC0]:0061FEB5 db  65h ; e
Stack[00004EC0]:0061FEB6 db  6Eh ; n
Stack[00004EC0]:0061FEB7 db  56h ; V
Stack[00004EC0]:0061FEB8 db  61h ; a
Stack[00004EC0]:0061FEB9 db  44h ; D
Stack[00004EC0]:0061FEBA db  69h ; i
Stack[00004EC0]:0061FEBB db    0
```

## Flag
- Ta thu được flag: `ATTT{XachBaloLenVaDi}`.

