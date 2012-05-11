Why .NET Won't Beat Java (Yet)
==============================

:date: 2009-06-23
:category: programming
:tags: .net, java

It's been no real secret that the .NET CLR (Common Language Runtime) has been Microsoft's answer to 
Java.  Garbage collection, bytecode compilation, large set of core libraries, it's all there.  But 
there is a problem that I've encountered recently: distribution size and install base.

A fairly clean Windows XP machine is fairly certain to not have anything higher than .NET 1.x 
installed.  Anything really compelling in the .NET framework requires 3.5.  This means somehow you 
need to get version 3.5 onto the machine somehow.  This isn't a problem in Windows Vista and later, 
which include the framework.  Microsoft's answer to simple deployment is it's "ClickOnce" system, 
where an application automatically installs .NET from the Internet (if necessary) before installing 
itself.  Sure, it's a 60MB download, but it only needs to be done once.

The real issue is when you can't guarantee an Internet connection or a working .NET 3.5 
installation.  At this point you must resort to the offline installation, and this is where .NET and 
Java are very different.  For Java 1.6 SE, the offline installer is 16MB for Windows 32-bit.  For 
.NET 3.5, the offline installer is a *200MB* universal package, with no way to cut out the parts you 
don't need.  Java in fact is so small relatively speaking that many applications actually include 
the JRE in their package (for example OpenOffice - 148MB with JRE vs. 134MB without), whereas .NET 
can turn a 10MB application into a 210MB monstrosity.

Now in my particular situation, I'm embarassed to have chosen to use C#/.NET/WPF for a simple tool 
at work.  For programming the tool itself, it was certainly the fastest option - other kinds of 
Windows programming, e.g. MFC or Forms, just look painful, and I thought the barrier to entry would 
be lower than Java.  However this 1MB tool requires the 200MB .NET offline installer to be carted 
around with it because the network it's used on is completely separate from the Internet.

.NET will only be *really* appealing once it's ubiquitous, but then "critical mass" is one of the 
big problems for lots of software. For now, I think I'm going to try Java next time...
