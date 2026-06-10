#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pdfplumber
import sys

# 确保输出为 UTF-8
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def analyze_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                full_text += text + "\n"
        
        # 写入文件
        with open("pdf_extracted_text.txt", "w", encoding="utf-8") as f:
            f.write(full_text)
        print("文本已保存到 pdf_extracted_text.txt")
        
        # 搜索日期相关行
        for line in full_text.split('\n'):
            line_lower = line.strip()
            # 搜索包含 "日期" 或类似字样的行
            if any(kw in line_lower for kw in ['日期', '测评', '时间']):
                print(f"[日期相关] {line.strip()}")
        
        # 搜索学生信息
        for line in full_text.split('\n'):
            line_stripped = line.strip()
            if any(kw in line_stripped for kw in ['姓名', '年级', '学校', '城市']):
                print(f"[学生信息] {line_stripped}")
        
        # 打印前500字符
        print("\n=== 前500字符 ===")
        print(full_text[:500])

if __name__ == "__main__":
    pdf_file = "杨扬-学习力综合测评 (前测) 测评报告 (1).pdf"
    analyze_pdf(pdf_file)
