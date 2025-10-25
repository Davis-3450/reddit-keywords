import gradio as gr


def web_ui():
    with gr.Blocks() as demo:
        gr.Markdown("Hello World")
    demo.launch()
