import os
import json

from openai import OpenAI


client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)



def analyze_image(image_url):

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {
                "role":"system",

                "content":
                """
                你是一個動漫周邊辨識助手。

                分析圖片中的動漫商品。

                回傳 JSON:
                {
                  "anime":"",
                  "character":"",
                  "product_type":"",
                  "confidence":0
                }

                不要輸出其他文字。
                """
            },


            {
                "role":"user",

                "content":[

                    {
                    "type":"text",
                    "text":
                    "辨識這張動漫周邊圖片"
                    },


                    {
                    "type":"image_url",

                    "image_url":
                    {
                    "url":image_url
                    }

                    }

                ]
            }

        ]

    )


    result = (
        response
        .choices[0]
        .message
        .content
    )


    return json.loads(result)
