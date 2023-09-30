decode:
   0x00000000000011c9 <decode+0>:     endbr64
   0x00000000000011cd <decode+4>:     push   rbp
   0x00000000000011ce <decode+5>:     mov    rbp,rsp
   0x00000000000011d1 <decode+8>:     mov    eax,edi
   0x00000000000011d3 <decode+10>:    mov    BYTE PTR [rbp-0x4],al
   0x00000000000011d6 <decode+13>:    movsx  eax,BYTE PTR [rbp-0x4]
   0x00000000000011da <decode+17>:    shl    eax,0x18
   0x00000000000011dd <decode+20>:    or     eax,0x495350
   0x00000000000011e2 <decode+25>:    pop    rbp
   0x00000000000011e3 <decode+26>:    ret

check: 
   0x00000000000011e4 <check+0>:     endbr64
   0x00000000000011e8 <check+4>:     push   rbp
   0x00000000000011e9 <check+5>:     mov    rbp,rsp
   0x00000000000011ec <check+8>:     sub    rsp,0xc0
   0x00000000000011f3 <check+15>:    mov    QWORD PTR [rbp-0xb8],rdi
   0x00000000000011fa <check+22>:    mov    rax,QWORD PTR fs:0x28
   0x0000000000001203 <check+31>:    mov    QWORD PTR [rbp-0x8],rax
   0x0000000000001207 <check+35>:    xor    eax,eax
   0x0000000000001209 <check+37>:    mov    DWORD PTR [rbp-0xa0],0x50495350
   0x0000000000001213 <check+47>:    mov    DWORD PTR [rbp-0x9c],0x54495350
   0x000000000000121d <check+57>:    mov    DWORD PTR [rbp-0x98],0x49495350
   0x0000000000001227 <check+67>:    mov    DWORD PTR [rbp-0x94],0x54495350
   0x0000000000001231 <check+77>:    mov    DWORD PTR [rbp-0x90],0x43495350
   0x000000000000123b <check+87>:    mov    DWORD PTR [rbp-0x8c],0x54495350
   0x0000000000001245 <check+97>:    mov    DWORD PTR [rbp-0x88],0x46495350
   0x000000000000124f <check+107>:   mov    DWORD PTR [rbp-0x84],0x7b495350
   0x0000000000001259 <check+117>:   mov    DWORD PTR [rbp-0x80],0x74495350
   0x0000000000001260 <check+124>:   mov    DWORD PTR [rbp-0x7c],0x6b495350
   0x0000000000001267 <check+131>:   mov    DWORD PTR [rbp-0x78],0x33495350
   0x000000000000126e <check+138>:   mov    DWORD PTR [rbp-0x74],0x5f495350
   0x0000000000001275 <check+145>:   mov    DWORD PTR [rbp-0x70],0x34495350
   0x000000000000127c <check+152>:   mov    DWORD PTR [rbp-0x6c],0x73495350
   0x0000000000001283 <check+159>:   mov    DWORD PTR [rbp-0x68],0x73495350
   0x000000000000128a <check+166>:   mov    DWORD PTR [rbp-0x64],0x33495350
   0x0000000000001291 <check+173>:   mov    DWORD PTR [rbp-0x60],0x6d495350
   0x0000000000001298 <check+180>:   mov    DWORD PTR [rbp-0x5c],0x62495350
   0x000000000000129f <check+187>:   mov    DWORD PTR [rbp-0x58],0x6c495350
   0x00000000000012a6 <check+194>:   mov    DWORD PTR [rbp-0x54],0x79495350
   0x00000000000012ad <check+201>:   mov    DWORD PTR [rbp-0x50],0x5f495350
   0x00000000000012b4 <check+208>:   mov    DWORD PTR [rbp-0x4c],0x66495350
   0x00000000000012bb <check+215>:   mov    DWORD PTR [rbp-0x48],0x30495350
   0x00000000000012c2 <check+222>:   mov    DWORD PTR [rbp-0x44],0x72495350
   0x00000000000012c9 <check+229>:   mov    DWORD PTR [rbp-0x40],0x5f495350
   0x00000000000012d0 <check+236>:   mov    DWORD PTR [rbp-0x3c],0x62495350
   0x00000000000012d7 <check+243>:   mov    DWORD PTR [rbp-0x38],0x33495350
   0x00000000000012de <check+250>:   mov    DWORD PTR [rbp-0x34],0x71495350
   0x00000000000012e5 <check+257>:   mov    DWORD PTR [rbp-0x30],0x6a495350
   0x00000000000012ec <check+264>:   mov    DWORD PTR [rbp-0x2c],0x6e495350
   0x00000000000012f3 <check+271>:   mov    DWORD PTR [rbp-0x28],0x6e495350
   0x00000000000012fa <check+278>:   mov    DWORD PTR [rbp-0x24],0x33495350
   0x0000000000001301 <check+285>:   mov    DWORD PTR [rbp-0x20],0x72495350
   0x0000000000001308 <check+292>:   mov    DWORD PTR [rbp-0x1c],0x5f495350
   0x000000000000130f <check+299>:   mov    DWORD PTR [rbp-0x18],0x72495350
   0x0000000000001316 <check+306>:   mov    DWORD PTR [rbp-0x14],0x33495350
   0x000000000000131d <check+313>:   mov    DWORD PTR [rbp-0x10],0x7d495350
   0x0000000000001324 <check+320>:   mov    DWORD PTR [rbp-0xac],0x0
   0x000000000000132e <check+330>:   mov    eax,DWORD PTR [rbp-0xac]
   0x0000000000001334 <check+336>:   cdqe
   0x0000000000001336 <check+338>:   mov    QWORD PTR [rbp-0xa8],rax
   0x000000000000133d <check+345>:   mov    rax,QWORD PTR [rbp-0xb8]
   0x0000000000001344 <check+352>:   mov    rdi,rax
   0x0000000000001347 <check+355>:   call   0x10a0 <checkstrlen@plt>
   0x000000000000134c <check+360>:   cmp    QWORD PTR [rbp-0xa8],rax
   0x0000000000001353 <check+367>:   jae    0x1399 <checkcheck+437>
   0x0000000000001355 <check+369>:   mov    eax,DWORD PTR [rbp-0xac]
   0x000000000000135b <check+375>:   movsxd rdx,eax
   0x000000000000135e <check+378>:   mov    rax,QWORD PTR [rbp-0xb8]
   0x0000000000001365 <check+385>:   add    rax,rdx
   0x0000000000001368 <check+388>:   movzx  eax,BYTE PTR [rax]
   0x000000000000136b <check+391>:   movsx  eax,al
   0x000000000000136e <check+394>:   mov    edi,eax
   0x0000000000001370 <check+396>:   call   0x11c9 <checkdecode>
   0x0000000000001375 <check+401>:   mov    edx,DWORD PTR [rbp-0xac]
   0x000000000000137b <check+407>:   movsxd rdx,edx
   0x000000000000137e <check+410>:   mov    edx,DWORD PTR [rbp+rdx*4-0xa0]
   0x0000000000001385 <check+417>:   cmp    eax,edx
   0x0000000000001387 <check+419>:   je     0x1390 <checkcheck+428>
   0x0000000000001389 <check+421>:   mov    eax,0x0
   0x000000000000138e <check+426>:   jmp    0x139f <checkcheck+443>
   0x0000000000001390 <check+428>:   add    DWORD PTR [rbp-0xac],0x1
   0x0000000000001397 <check+435>:   jmp    0x132e <checkcheck+330>
   0x0000000000001399 <check+437>:   nop
   0x000000000000139a <check+438>:   mov    eax,0x1
   0x000000000000139f <check+443>:   mov    rdx,QWORD PTR [rbp-0x8]
   0x00000000000013a3 <check+447>:   sub    rdx,QWORD PTR fs:0x28
   0x00000000000013ac <check+456>:   je     0x13b3 <checkcheck+463>
   0x00000000000013ae <check+458>:   call   0x10b0 <check__stack_chk_fail@plt>
   0x00000000000013b3 <check+463>:   leave
   0x00000000000013b4 <check+464>:   ret
