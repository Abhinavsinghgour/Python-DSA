{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMnsfyjL5tSPUxjqVTY/JiB",
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
        "<a href=\"https://colab.research.google.com/github/Abhinavsinghgour/Python-DSA/blob/main/Abhinav_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#*Sorting*"
      ],
      "metadata": {
        "id": "eAuzc1B5BZo1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Bubble_sort\n",
        "# Time complexity: O(n2)\n",
        "# Space complexity: O(1)\n",
        "a=[2,4,5,3,7,6]\n",
        "def bubble_sort(arr):\n",
        "  n=len(arr)\n",
        "  flag=True\n",
        "  while flag:\n",
        "    flag=False\n",
        "    for i in range(1,n):\n",
        "      if arr[i-1]>arr[i]:\n",
        "        flag=True\n",
        "        arr[i-1],arr[i]=arr[i],arr[i-1]\n",
        "\n",
        "bubble_sort(a)\n",
        "a\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gHd0tuw_BfwW",
        "outputId": "029f4fea-bb8f-4656-9ac1-422e852d4998"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[2, 3, 4, 5, 6, 7]"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Built-in sort function\n",
        "a=[2,4,5,3,7,6]\n",
        "a.sort(reverse=1)\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xiSDQM5HIfRh",
        "outputId": "a2cc4036-468f-4086-e026-201589461ef8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[7, 6, 5, 4, 3, 2]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Bubble_sort\n",
        "# Time complexity: O(n2)\n",
        "# Space complexity: O(1)\n",
        "def sort(arr):\n",
        "  n=len(arr)\n",
        "  for j in range(n-1,0,-1):\n",
        "    for i in range(j):# iterate j no. of times\n",
        "      if arr[i]>arr[i+1]:\n",
        "        arr[i],arr[i+1]=arr[i+1],arr[i]\n",
        "\n",
        "a=[2,4,5,3,7,6]\n",
        "sort(a)\n",
        "a\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3jRUlpefJQpk",
        "outputId": "5a1ce237-e10d-4d32-f884-63a70abd9e3c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[2, 3, 4, 5, 6, 7]"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a=[2, 3, 4, 5, 6, 7]\n",
        "for i in range(len(a)):\n",
        "  print(a[i],i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c2GHOQV7OcNN",
        "outputId": "448d4edd-8c20-4e60-f777-356eb24f5a54"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 0\n",
            "3 1\n",
            "4 2\n",
            "5 3\n",
            "6 4\n",
            "7 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def selection_sort(arr):\n",
        "  for i in range(len(arr)-1):\n",
        "    min_idx=i\n",
        "    # print(min_idx)\n",
        "    for j in range(i+1,len(arr)):\n",
        "      if arr[j]<arr[min_idx]:\n",
        "        min_idx=j\n",
        "\n",
        "    arr[i],arr[min_idx]=arr[min_idx],arr[i]\n",
        "\n",
        "a=[2,4,5,3,7,6]\n",
        "selection_sort(a)\n",
        "print(a)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ntm1AaXKx7Zg",
        "outputId": "72fe5f48-b9ec-4e1d-c637-342157684f42"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2, 3, 4, 5, 6, 7]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# *Merge sort*"
      ],
      "metadata": {
        "id": "DpNEdA--ZBgp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Merge Sort\n",
        "# Merge Sort is an efficient sorting algorithm with O(nlogn) running time.\n",
        "def merge_sort(arr):\n",
        "  if len(arr)>1:\n",
        "    left_arr=arr[:len(arr)//2]\n",
        "    right_arr=arr[len(arr)//2:]\n",
        "\n",
        "    #recursion\n",
        "    merge_sort(left_arr)\n",
        "    merge_sort(right_arr)\n",
        "\n",
        "    #merge\n",
        "    i=0 #left_arr_idx\n",
        "    j=0 #Right_arr_idx\n",
        "    k=0 #merge_arr_idx\n",
        "    while(i<len(left_arr) and j<len(right_arr)):\n",
        "      if left_arr[i]<right_arr[j]:\n",
        "        arr[k]=left_arr[i]\n",
        "        i+=1\n",
        "      else:\n",
        "        arr[k]=right_arr[j]\n",
        "        j+=1\n",
        "      k+=1\n",
        "    while i<len(left_arr):\n",
        "       arr[k]=left_arr[i]\n",
        "       i +=1\n",
        "       k+=1\n",
        "    while j<len(right_arr):\n",
        "       arr[k]=right_arr[j]\n",
        "       j+=1\n",
        "       k+=1\n",
        "\n",
        "arr = [2,3,5,1,7,4,4,4,2,6,8]\n",
        "merge_sort(arr)\n",
        "print(arr)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "koAEOUDaY-Gz",
        "outputId": "4b72ff10-78bf-45dc-9152-6bb395b4d70e"
      },
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 8]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "iUy6QZQGyBK3"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
