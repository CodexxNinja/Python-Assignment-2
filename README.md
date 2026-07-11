<h2><img src="https://media.giphy.com/media/L8K62iDadbixW/giphy.gif" width="40" align="center" alt="Book"> ~ About The Project</h2>

Welcome to **Python Assignment 2**! This repository is engineered to be a comprehensive, hands-on playground for developers looking to solidify their understanding of Python's most powerful built-in features. By diving into this repository, you are exploring the core DNA of Python programming. We focus on modular design, data sequencing, and high-speed key-value mapping. Every folder is packed with practical scripts that transition you from theoretical concepts to real-world application building.

<hr>

<h2><img src="https://media.giphy.com/media/26tn33aiTi1jVDzO0/giphy.gif" width="40" align="center" alt="Target"> Core Learning Objectives</h2>

We have structured this repository to ensure you walk away with highly applicable skills. Instead of just reading about Python, you will be interacting with code that demonstrates industry-standard practices. hjg

| 🚀 Objective Category | 🧠 What You Will Master |
| :--- | :--- |
| **Architectural Modularity** | Structuring code using Functions to adhere to the DRY (Don't Repeat Yourself) principle. Managing scopes and memory effectively. |
| **Data Sequencing** | Harnessing Python Lists to traverse, slice, sort, and mutate massive amounts of ordered data efficiently. |
| **Hash Mapping** | Utilizing Dictionaries to build high-performance data retrieval systems and modeling complex, real-world entities. |

<hr>

<h2><img src="https://media.giphy.com/media/3o7TKMt1VVNkHV2PaE/giphy.gif" width="40" align="center" alt="Files"> Deep Dive: Module Breakdown</h2>

<h3 align="left">
  <img src="https://media.giphy.com/media/Wn74RUT0vjnoU98Hnt/giphy.gif" width="30" align="center" alt="Gears"> 1. Function in Python
</h3>

Functions represent the foundation of scalable software. This module explores how to encapsulate logic so it can be invoked anywhere in your architecture. You will explore positional mapping, keyword arguments, and the power of anonymous throwaway functions.

| Concept | Description & Application |
| :--- | :--- |
| **Defining & Calling** | Creating reusable blocks using the `def` keyword and yielding outputs. |
| **Argument Unpacking** | Utilizing `*args` and `**kwargs` to allow functions to accept an infinite number of parameters dynamically. |
| **Lambda Expressions** | Writing inline, anonymous functions for rapid data transformations (e.g., inside `map()` or `filter()`). |
| **Scope Management** | Navigating the LEGB rule (Local, Enclosing, Global, Built-in) to prevent variable collision. |

> **Mini Example:**
> ```python
> def ninja_greeting(name, weapon="Katana"):
>     return f"Hello {name}, your {weapon} is ready!"
> ```

<h3 align="left">
  <img src="https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif" width="30" align="center" alt="List"> 2. List in Python
</h3>

Lists are the ultimate Swiss Army knife of Python data structures. They are mutable, dynamic, and capable of holding heterogeneous data types. This section teaches you how to push lists to their limits.

| Concept | Description & Application |
| :--- | :--- |
| **Advanced Slicing** | Extracting precise sub-segments of data using `[start:stop:step]` syntax, including deep reversing. |
| **In-Place Mutation** | Modifying lists in memory using `.append()`, `.extend()`, `.insert()`, and `.pop()` without creating new objects. |
| **Comprehensions** | Replacing multi-line `for` loops with single-line, highly optimized list comprehensions. |
| **Multi-Dimensional Arrays** | Constructing and iterating through 2D lists (matrices) for complex data grids. |

> **Mini Example:**
> ```python
> ninja_scores = [85, 92, 78, 99]
> passed_ninjas = [score for score in ninja_scores if score > 80]
> ```

<h3 align="left">
  <img src="https://media.giphy.com/media/l41lOlmIQJEdJusM0/giphy.gif" width="30" align="center" alt="Dict"> 3. Python Dictionaries
</h3>

When you need instantaneous data lookups, Dictionaries are the answer. Powered by hash tables, dictionaries allow you to map unique keys to complex values. This directory explores JSON-like data structuring.

| Concept | Description & Application |
| :--- | :--- |
| **Key-Value Construction** | Building dictionaries and understanding why keys must be immutable types (like strings or tuples). |
| **Safe Extraction** | Using the `.get()` method to retrieve data safely without triggering `KeyError` exceptions. |
| **Dictionary Iteration** | Looping through massive data structures using `.items()`, `.keys()`, and `.values()`. |
| **Modern Merging** | Combining multiple dictionaries seamlessly (including the modern Python 3.9+ `|` merge operator). |

> **Mini Example:**
> ```python
> ninja_profile = {"name": "Codexx", "rank": "Master", "stealth": 100}
> current_rank = ninja_profile.get("rank", "Unknown")
> ```

<hr>

<h2><img src="https://media.giphy.com/media/Y4vBiFdqtGsDu/giphy.gif" width="40" align="center" alt="Rocket"> Getting Started & Installation</h2>
