import gradio as gr
from rembg import remove
from PIL import Image

def process_image(input_image):
    if input_image is None:
        return None
    # 執行去背
    output_image = remove(input_image)
    return output_image

# 建立介面
demo = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="pil", label="上傳圖片"),
    outputs=gr.Image(type="pil", label="去背成品"),
    title="快速去背工具",
    description="上傳圖片即可獲得透明背景的 PNG 檔案。"
)

if __name__ == "__main__":
    demo.launch()
