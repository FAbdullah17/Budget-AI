import os
import pandas as pd

def summarize_transaction_file(file_path: str) -> str:
    if not os.path.exists(file_path):
        return "The file path is invalid or the file does not exist."

    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith((".xls", ".xlsx")):
            df = pd.read_excel(file_path)
        else:
            return "Unsupported file format. Upload CSV or Excel only."

        if df.empty or df.shape[1] < 2:
            return "The uploaded file is empty or invalid."

        output = []

        if "Amount" in df.columns:
            df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
            df = df.dropna(subset=["Amount"])

            spent = df[df["Amount"] < 0]["Amount"].sum()
            received = df[df["Amount"] > 0]["Amount"].sum()
            avg = df["Amount"].mean()
            largest_expense = df[df["Amount"] < 0]["Amount"].min()
            largest_income = df[df["Amount"] > 0]["Amount"].max()

            output.extend([
                f"Total Spent: {abs(spent):.2f}",
                f"Total Received: {received:.2f}",
                f"Average Transaction: {avg:.2f}",
                f"Largest Expense: {abs(largest_expense):.2f}",
                f"Largest Income: {largest_income:.2f}",
            ])

        if "Category" in df.columns:
            top_cats = df.groupby("Category")["Amount"].sum().sort_values().head(3)
            output.append("Top Spending Categories:")
            output.extend([f" - {cat}: {amount:.2f}" for cat, amount in top_cats.items()])

        return "\n".join(output)

    except Exception as e:
        return f"Failed to process the file: {str(e)}"
