# 3. Change one thing and save

## Ask AI to change the chart

Return to the same AI chat and send this follow-up.

```text
Please change the bars to green and set the chart title to "Milk samples".
Keep the same four samples, counts and mean calculation.
Return the complete updated R code.
```

Copy the new code. In your RStudio script editor, select all the old code and paste the new reply over it. Select the new code and click **Run**.

The mean should still be **25**. The chart should now have green bars and the title **Milk samples**.

![Reference chart with green bars and the title Milk samples.](../outputs/reference/green-chart.png)

````{admonition} Example of the updated code
:class: note dropdown

```r
counts <- c(10, 20, 30, 40)
mean(counts)

barplot(counts,
        names.arg = c("A", "B", "C", "D"),
        main = "Milk samples",
        ylab = "Count (CFU/mL)",
        col = "seagreen3")
```
````

## Save your script

In RStudio, choose **File → Save As**. Pick a folder you can find again, such as **Documents**, and name the file **my-first-r.R**.

Use **Ctrl + S** on Windows or **Cmd + S** on macOS to save later changes. You can open this file again with **File → Open File** in RStudio.

**You have finished** when you have asked AI for code, run it, seen the changed chart and saved **my-first-r.R**.
