# 1. Ask AI for code

Keep RStudio open. In your web browser, open **HKU GenAI** and sign in with your **HKU Portal account**. Choose a text model and start a new chat. [Open HKU GenAI](https://genai.hku.hk/)

Copy this whole prompt into the chat and send it.

```text
I am new to R and I am using RStudio.

Create four invented milk samples called A, B, C and D.
Their counts are 10, 20, 30 and 40 CFU/mL.
Calculate the mean and show it in the Console.
Draw a bar chart with the sample names and a y-axis labelled "Count (CFU/mL)".

Use base R so I can run the code directly.
Return one complete R code block.
```

Wait for a reply containing R code. Use the **Copy** button on that code box. You will paste it into a script in the next step.

```{admonition} HKU allowance and other chats
:class: note dropdown

HKU provides an AI allowance for students. As checked on 7 November 2026, ITS lists **500,000 AI Credits per month**. Your balance appears in the app. [HKU ITS information](https://its.hku.hk/services/ai-as-a-service/hku-genai/)

If you prefer another service or cannot sign in, try one of these browser chats. [Google Gemini](https://gemini.google.com/) · [Microsoft Copilot](https://copilot.com/) · [Poe](https://poe.com/)
```

**Next.** [Paste your code into RStudio and run it](02-copy-and-run.md).
