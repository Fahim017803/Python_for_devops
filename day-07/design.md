# Day 07 – Thinking Before Coding

## Script Selected
Python CLI Log Analyzer (Day-06)

---

## What problem am I solving?

Server বা application এর log file অনেক বড় হয়।
হাতে ধরে log পড়া সময় নেয় এবং ভুল হওয়ার সম্ভাবনা থাকে।

এই স্ক্রিপ্টের কাজ হলো:
- log file থেকে INFO, WARNING, ERROR গুনে বের করা
- দ্রুত একটা summary দেখানো

---

## What input does my script need?

User terminal থেকে input দেবে:

- Log file এর path  
  Example:
  --file input.txt

- (Optional) Output file এর নাম  
  Example:
  --out summary.txt

স্ক্রিপ্ট user এর কাছে interactive input চাইবে না।

---

## What output should my script give?

### Terminal এ:
- INFO কতটি
- WARNING কতটি
- ERROR কতটি

Example:
INFO: 4  
WARNING: 3  
ERROR: 3  

### Output file এ:
- একই summary একটি text file এ লেখা হবে

---

## What are the main steps?

1. User CLI command চালাবে
2. Script input log file খুলবে
3. INFO, WARNING, ERROR count করবে
4. Result terminal এ দেখাবে
5. Result output file এ লিখবে
6. File না পেলে error message দেখাবে

---

## Summary

Coding করার আগে আমি:
- সমস্যাটা বুঝেছি
- input ও output পরিষ্কার করেছি
- ধাপে ধাপে কী হবে সেটা লিখেছি

এইভাবে plan করলে automation কম ভুল করবে।
