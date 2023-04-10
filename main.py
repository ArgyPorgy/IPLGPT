from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import csv
import openai
import urllib.parse
import sys
import traceback


import tkinter as tk
import openai

openai.api_key = "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"

model_name = "curie:ft-personal-2023-03-30-19-17-15"

def on_submit():
    prompt = input_field.get()

    completion = openai.Completion.create(model=model_name, prompt=prompt,max_tokens=100)

    input_field.delete(0, "end")
    text = completion.choices[0].text

    result_text.config(state="normal")
    result_text.delete("1.0", "end")
    result_text.insert("end", text)
    result_text.config(state="disabled")

window = tk.Tk()
window.title("IPL GPT")

input_field = tk.Entry(window)
submit_button = tk.Button(window, text="Submit", command=on_submit)
result_text = tk.Text(window, state="disabled", width=80, height=20)

input_field.pack()
submit_button.pack()
result_text.pack()

window.mainloop()


