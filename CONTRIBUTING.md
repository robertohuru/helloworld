## How to contribute to CB-FLTS

#### **Did you find a bug?**

* **Ensure the bug was not already reported** by searching on GitHub under [Issues](https://github.com/robertohuru/helloworld/issues/).

* If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/robertohuru/helloworld/issues/new?template=bug-reporting-form.yml) using the template provided. Be sure to include a **title and clear description**, as much relevant information as possible, and a **screenshots**, and a **reproduction steps** demonstrating how the steps that led to the unexpected behavior.

* We recommend using the template. However, you can also [open a blank issue](https://github.com/robertohuru/helloworld/issues/new). Ensure you fill in as much details as possible including a **title and clear description**, and attach **screenshots** if necessary.


#### **Did you write a patch that fixes a bug?**

* Open a new GitHub pull request (PR) with the patch.

* Ensure the PR description clearly describes the problem and solution. Include the relevant issue number if applicable.

* Before submitting, please read the **Coding Convention** below to know more about our coding styles and benchmarks.


#### **Do you intend to suggest/add a new feature or change an existing one?**

* Suggest your change using the [feature request form](https://github.com/robertohuru/helloworld/issues/new?template=feature_request.yml). Ensure you fill the all the required fields and provide as much relevant information as possible.

* You can also use the [use case form](https://github.com/robertohuru/helloworld/issues/new?template=use-case-form.yml) to suggest new system requirements. You will be required to supply additional information such as **actors, description, preconditions, trigger, business rules**, among others.


### **Coding Convention**

We don't like reinventing the wheel. So, our coding standards uses the [PEP 8 -- Style Guide](https://www.python.org/dev/peps/pep-0008/). We optimize for readability. Just a few mentions:

  * We indent using two spaces (soft tabs)
  * We use Pylint for finding bugs and style problems in our source code. Make sure you run pylint on your code. Suppress warnings if they are inappropriate so that other issues are not hidden. To suppress warnings, you can set a line-level comment. Please know that when you commit you code, we will run an automatic pylint test to ensure that there are no issues.
  * We avoid avoid global variables. Variables that are declared at the module level or as class attributes.
  * Maximum line length is 80 characters. Exception to this rule is when you have long import statements, URLs, pathnames, or long flags in comments.
  * Be sure to use the right style for class, function, method docstrings and inline comments.
  * Don't import modules like this, [`from module import *`]. Instead list the names you need explicitly e.g [`from module import method1, method2`]
  * We ALWAYS put spaces after list items and method parameters (`[1, 2, 3]`, not `[1,2,3]`), around operators (`x += 1`, not `x+=1`), and around hash arrows.
  * This is open source software. Consider the people who will read your code, and make it look nice for them. It's sort of like driving a car: Perhaps you love doing donuts when you're alone, but with passengers the goal is to make the ride as smooth as possible.
  

Thanks! :heart: :heart: :heart:

CB-FLTS Team
