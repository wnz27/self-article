<!--
 * @Date: 2020-09-27 14:50:40
 * @LastEditTime: 2020-09-27 15:02:42
-->

# python3-csv写入中文打开乱码的问题

原始使用：
`csv_file = open(csv_file_name, 'w')`
> 会导致有些windows用户用excel打开生成的csv，内容里中文是乱码的情况。
现在使用：
`csv_file = open(csv_file_name, 'w', encoding="utf-8-sig")`
> 这时候生成的csv，用excel打开后中文不再是乱码。

# csv-导入长串数字字符串不显示科学计数法的小技巧

`"{}'".format(long_num_str)`
事实上，前后加单个都行。
