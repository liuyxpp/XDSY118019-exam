# 期末考试第二部分 提交包

- 课程：跨入科学研究之门（XDSY118019）
- 学号：26800190065
- 姓名：BruceGao
- 日期：2026-11-19

## 内容

- `exam_part2.md`：四道题的完整答案（Markdown 源文件）
- `exam_part2_26800190065_BruceGao.pdf`：上述文件的渲染结果
- `minkowski.py`：第1题修改后的 Python 源码
- `part2_solution/`：第1—3题的计算/绘图源码与图片

## 复现

```bash
python -m doctest minkowski.py          # 第1题 docstring 用例
python part2_solution/q1_distances.py   # 第1题三组距离
python part2_solution/q2_klein.py       # 第2题 Python 等价渲染
python part2_solution/q3_verify.py      # 第3题 SymPy 验证
```

第2题 `q2_klein.m` 在 MATLAB 中运行（R2020b+）；第3题 `q3_series_integral.wl` 在
Wolfram Mathematica 中运行。
