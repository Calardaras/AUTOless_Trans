AUTOless_Trans 并不能自动的机翻
==================================
自用p社游戏汉化分割工具，以适配第三方翻译工具(有道、DeepL)的文档翻译功能
目前对有复杂子文件夹的情形有bug

用法
-----------------------------------
1.将localization里的english文件夹放入original，运行compose.py<br>
2.手动将生成在process文件夹内的vaule.docx交由第三方翻译器翻译，并更名为tr_va放回<br>
3.运行decompose.py，输出结果在output内<br>

已有特性
--------------------------------------
1) 遍历子文件夹 *
2) 自动以1w或5k字分割word文档
3) 提取无格式的文本 
4) 恢复文本格式 

关于格式的碎碎念
-----------------
就p社的localization而言，格式是指诸如：
1) #Y 字段 #!      其内部字段需要翻译！
2) \[scope.name\]  其内部字段必须完整保留！
3) $字段$          其内部字段必须完整保留！
4) \n              建议完整保留
normalize.py能提取出无格式字符。将无需翻译的部分以通配符<αωα>的形式保留，并保存引索。
formalize.py用以还原原始格式。但由于中英语序的问题，仅仅按照英文引索恢复出的中文有可能在语言逻辑上是错的。
如果报错，大概率是在翻译过程中对通配符<αωα>进行的删改，可以按行号检查一下。


代办集
-----------------------------------
1) 更自动化
2) 优化逻辑

