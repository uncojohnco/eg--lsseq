# test--dd-2019

## The Problem:

A directory at Digital Domain might contain hundreds or even thousands of image files. Doing an &quot;ls&quot; in this directory will produce a difficult to handle listing of all these files.

For example, here is an ls of a small directory.

```bash
> ls
elem.info sd_fx29.0112.rgb sd_fx29.0125.rgb sd_fx29.0137.rgb
sd_fx29.0101.rgb sd_fx29.0113.rgb sd_fx29.0126.rgb sd_fx29.0138.rgb
sd_fx29.0102.rgb sd_fx29.0114.rgb sd_fx29.0127.rgb sd_fx29.0139.rgb
sd_fx29.0103.rgb sd_fx29.0115.rgb sd_fx29.0128.rgb sd_fx29.0140.rgb
sd_fx29.0104.rgb sd_fx29.0116.rgb sd_fx29.0129.rgb sd_fx29.0141.rgb
sd_fx29.0105.rgb sd_fx29.0117.rgb sd_fx29.0130.rgb sd_fx29.0142.rgb
sd_fx29.0106.rgb sd_fx29.0118.rgb sd_fx29.0131.rgb sd_fx29.0143.rgb
sd_fx29.0107.rgb sd_fx29.0119.rgb sd_fx29.0132.rgb sd_fx29.0144.rgb
sd_fx29.0108.rgb sd_fx29.0120.rgb sd_fx29.0133.rgb sd_fx29.0145.rgb
sd_fx29.0109.rgb sd_fx29.0121.rgb sd_fx29.0134.rgb sd_fx29.0146.rgb
sd_fx29.0110.rgb sd_fx29.0123.rgb sd_fx29.0135.rgb sd_fx29.0147.rgb
sd_fx29.0111.rgb sd_fx29.0124.rgb sd_fx29.0136.rgb strange.xml
```

Did you notice that the file sd_fx29.0122.rgb was missing? Neither did I!

What we&#39;d rather have is a listing that looks like this:
```bash
> lss
1 elem.info
46 sd_fx29.%04d.rgb 101-121 123-147
1 strange.xml
```
It requires a bit of familiarity with C style printf formatting on the user&#39;s part, 
but once they get used to it, it&#39;s great!


## The Assignment:

Implement the &quot;lss&quot; command in Python.

The command needs to accept one optional argument: a path to the directory or file, similar to the &quot;ls&quot; command.

- Make it as general as possible. 
- The goal is to find sequences of files that can be concatenated together. 
- Please don&#39;t rely on specific characters as delimiters since we can&#39;t control how artists name their files.
- And don&#39;t assume anything about the zero-padding.

Beware, we will try your command on some tricky directories, like:
```bash
alpha.txt
file01_0040.rgb
file01_0041.rgb
file01_0042.rgb
file01_0043.rgb
file02_0044.rgb
file02_0045.rgb
file02_0046.rgb
file02_0047.rgb
file1.03.rgb
file2.03.rgb
file3.03.rgb
file4.03.rgb
file.info.03.rgb
```

It should produce:
```bash
> lss
1 alpha.txt
4 file01_%04d.rgb 40-43
4 file02_%04d.rgb 44-47
4 file%d.03.rgb 1-4
1 file.info.03.rgb
```

- We encourage the use of existing code to make this assignment easier.
- Using a regular expression library, file system calls, interesting data structures and more are all fair game. 
- (Though if you find an implementation of lss out on the net, we&#39;d appreciate you not looking at it. That&#39;s taking code reuse a little too far :-) ) 
- For Python, the standard library should be more than sufficient.

- We will be examining your code for 
  - clarity, 
  - correctness,
  - and efficiency. 
- We are using this to see how you go about solving a problem. 
- There is a time limit of 7 days from the day received. 
- We will wait on the return of this before proceeding.

If anything isn&#39;t clear, please feel free to ask questions. 
That is, after all, part of the problem solving process.

Good Luck
