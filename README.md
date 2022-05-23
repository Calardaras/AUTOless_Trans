AUTOless_Trans 并不能自动的机翻
==================================
自用p社游戏汉化分割工具，以适配第三方翻译工具(有道、DeepL)的文档翻译功能
目前对有复杂子文件夹的情形有bug

用法
-----------------------------------
！！永远别机翻地名！！
![image](https://github.com/Calardaras/AUTOless_Trans/blob/main/howtouse/readme.jpg)

测试项目
-----------------------------------
名称 总词条 格式错误 占比
Invictus 33,830 843 2.4327600138520147%。

效果我还算满意

已有特性
--------------------------------------
1) 遍历子文件夹 *
2) 自动以1w或5k字分割word文档
3) 提取无格式的文本 
4) 恢复文本格式 

关于格式的碎碎念
-----------------
就p社的localization而言，格式是指诸如下列所示的字符：
1) #[YGRTFE!]{1,2}      标记后续文本的颜色，必须完整保留！
2) \[.+?\]              必须完整保留！
3) \$.+?                必须完整保留！
4) \n                   建议完整保留

normalize.py能提取出无格式字符。将无需翻译的部分以通配符<αωα>的形式保留，并保存引索。<br>
formalize.py用以还原原始格式。但由于中英语序的问题，仅仅按照英文引索恢复出的中文有可能在语言逻辑上是错的。<br>
如果报错，大概率是在翻译过程中对通配符<αωα>进行的删改，可以按行号检查一下。<br>


代办集
-----------------------------------
1) 更自动化
2) 优化逻辑

