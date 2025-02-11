  0x00000000004013ff <+276>:   mov    rax,QWORD PTR [rip+0x2c1a]        # 0x404020 <stdout@GLIBC_2.2.5>
   0x0000000000401406 <+283>:   mov    esi,0x0
   0x000000000040140b <+288>:   mov    rdi,rax
   0x000000000040140e <+291>:   call   0x4010a0 <setbuf@plt>
   0x0000000000401413 <+296>:   mov    eax,0x0
   0x0000000000401418 <+301>:   call   0x4012b5 <vuln>
   0x000000000040141d <+306>:   mov    eax,0x0
   0x0000000000401422 <+311>:   pop    rbp

   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA