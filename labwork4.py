{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNk/pmbbQ/3MAXyg1dNlNH8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/antk2510007-sudo/Python-2026-L1/blob/main/labwork4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "6d4ECl1n8sCs"
      },
      "outputs": [],
      "source": [
        "import math\n",
        "import numpy as np\n",
        "\n",
        "class Student:\n",
        "    def __init__(self, id, name, dob):\n",
        "        self.id = id\n",
        "        self.name = name\n",
        "        self.dob = dob\n",
        "        self.marks = []\n",
        "    def add_mark(self, mark):\n",
        "        self.marks.append(math.floor(mark * 10) / 10)\n",
        "    def gpa(self, credits):\n",
        "        return np.average(self.marks, weights=credits)\n",
        "\n",
        "\n",
        "class Course:\n",
        "    def __init__(self, id, name, credits):\n",
        "        self.id = id\n",
        "        self.name = name\n",
        "        self.credits = credits\n",
        "\n",
        "def input_students():\n",
        "    students = []\n",
        "    n = int(input(\"Number of students: \"))\n",
        "    for i in range(n):\n",
        "        s = Student(\n",
        "            input(\"ID: \"),\n",
        "            input(\"Name: \"),\n",
        "            input(\"DOB: \")\n",
        "        )\n",
        "        for j in range(3):\n",
        "            s.add_mark(float(input(\"Mark: \")))\n",
        "        students.append(s)\n",
        "    return students\n",
        "\n",
        "\n",
        "def show_students(students, credits):\n",
        "    print(\"\\n===== STUDENTS ====\")\n",
        "    students.sort(\n",
        "        key=lambda s: s.gpa(credits),\n",
        "        reverse=True\n",
        "    )\n",
        "    for s in students:\n",
        "        print(s.id, s.name, \"GPA:\", s.gpa(credits))\n",
        "\n",
        "\n",
        "\n",
        "credits = [3, 3, 4]\n",
        "\n",
        "students = input_students()\n",
        "\n",
        "show_students(students, credits)\n",
        "\n"
      ]
    }
  ]
}