
# What a computer is actually doing

Before we talk about servers, deployments, or any of the CI/CD stuff, it helps to
get really concrete about what a computer is doing when you run a program.


# Components of a computer

### Introduction

Before we talk about servers, deployments, or any of the CI/CD stuff, it helps
to get really concrete about what a computer is, what its important
components are, and what it's actually doing when you run a program.

### What is a computer

Historically, **_"Computer"_** meant a person who did computations by hand. In the
past, that was often women doing calculations for engineering, astronomy, and
science. Today the term universally refers to automated electronic machinery.

**The modern definition:** A computer is a programmable electronic machine that
accepts raw data, processes it using instructions, stores information, and
outputs a result.

Every modern computer is built from a combination of components that work
together to process, store, and display information. Below is a breakdown of
the essential ones.

### 1. Motherboard

A large flat circuit board that acts as the central hub of the computer.
Every other component connects to it. CPU, memory, storage, network card,
power supply. Its main role is facilitating communication between all these
components, passing electrical signals and data back and forth between them.

Think of it like a city's road network — it doesn't *do* any of the work
itself, but without it, nothing else can talk to anything else.


### 2. CPU (Central Processing Unit). The "Processor"

The CPU is what actually *does* the work. It executes instructions, one
after another, extremely fast (modern CPUs handle billions of instructions
per second). Every calculation, every decision your program makes, every line
of code you write eventually gets broken down into instructions the CPU
carries out.


### 3. RAM (Random Access Memory). Short-term memory

RAM is fast, temporary storage. Whatever your program is actively working
with *right now* — variables, open files, data mid-calculation — lives here.

The key trade-off: RAM is very fast, but it's **wiped when the power turns
off**. Nothing in RAM survives a restart.


### 4. Storage (Disk). Long-term memory

Storage (a hard drive, or more commonly today an SSD) is where things live
*permanently*. Your files, your installed programs, your code, your photos.
Unlike RAM, this data survives even after the computer is turned off.


### 5. Network interface

The component that lets a computer talk to other computers — over Wi-Fi, or
a wired connection. Every request you send (loading a webpage, sending a
message) and every response you receive travels through this.

This is the piece that becomes especially important once we talk about
servers. A server's entire job depends on its network interface constantly
receiving and responding to requests.


---

### How these work together

Say you run a simple program that adds two numbers:

1. The program's instructions and data are read from **storage**
2. They get loaded into **RAM** so they're quick to access
3. The **CPU** executes the instructions, does the addition
4. The result might get saved back to **storage**, sent over the **network**,
   or just displayed on screen
5. The **motherboard** is what physically connects all of this the entire
   time, carrying the signals between each component

Every computer you'll ever touch your laptop, your phone, a server sitting
in a data center has some version of these six things.

---

## What an Operating System (OS) is

You never talk to the CPU, RAM, or storage directly yourself. Instead, there's
a layer of software sitting between you and the hardware, managing all of it —
that's the **Operating System** (Windows, macOS, or Linux, most commonly).

The OS's job:

- Decides which program gets to use the CPU, and when (your laptop is running
  dozens of programs "at once," but really the CPU is rapidly switching
  between them, giving each a tiny slice of time)
- Manages RAM — making sure one program can't just take all of it, or read
  another program's data
- Reads and writes files to storage on a program's behalf
- Handles network requests coming in and going out

**Why this matters for later:** every program you run — including a
"server" — needs an OS underneath it to actually execute. When we talk later
about renting a server from AWS, what you're really renting is a computer,
with an OS already running on it, waiting for you to put your program on it.

### A useful mental model

Think of the whole computer like a restaurant kitchen:

- **CPU** = the chef, actually cooking
- **RAM** = the counter space where ingredients sit *right now*, mid-recipe
- **Storage** = the pantry/fridge — where everything lives long-term
- **Motherboard** = the pipework and wiring connecting every station
- **Network interface** = the phone line taking incoming orders and calling
  them back out once ready
- **OS** = the kitchen manager — deciding which order the chef works on next,
  making sure two dishes don't collide, keeping track of where everything is

---

**Next:** [What a server is](./02-what-is-a-server.md)