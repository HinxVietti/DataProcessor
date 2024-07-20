class DataSaver:
    def save_csv(self, df, file_path):
        df.to_csv(file_path, index=False)

    def save_excel(self, df, file_path):
        df.to_excel(file_path, index=False)
