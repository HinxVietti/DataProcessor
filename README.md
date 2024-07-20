# DataProcessor

`DataProcessor` is a Python package designed to handle various data processing tasks such as reading data from different sources, cleaning data, transforming data, and saving data to various formats.

## Features

- **Data Reading**: Read data from CSV and Excel files.
- **Data Cleaning**: Clean data by removing missing values.
- **Data Transformation**: Transform data by adding new columns.
- **Data Saving**: Save data to CSV and Excel files.

## Installation

To install the `DataProcessor` package, you can use `pip`:

```sh
pip install DataProcessor
```

## Usage

Here's a quick guide on how to use the `DataProcessor` package:

### Reading Data

```python
from data_processor.reader import DataReader

reader = DataReader()
df_csv = reader.read_csv('path/to/your/file.csv')
df_excel = reader.read_excel('path/to/your/file.xlsx')
```

### Cleaning Data

```python
from data_processor.cleaner import DataCleaner

cleaner = DataCleaner()
cleaned_df = cleaner.clean_data(df_csv)
```

### Transforming Data

```python
from data_processor.transformer import DataTransformer

transformer = DataTransformer()
transformed_df = transformer.transform_data(cleaned_df)
```

### Saving Data

```python
from data_processor.saver import DataSaver

saver = DataSaver()
saver.save_csv(transformed_df, 'path/to/your/output.csv')
saver.save_excel(transformed_df, 'path/to/your/output.xlsx')
```

## Example

Here's a complete example that demonstrates the entire workflow:

```python
from data_processor.reader import DataReader
from data_processor.cleaner import DataCleaner
from data_processor.transformer import DataTransformer
from data_processor.saver import DataSaver

# Initialize classes
reader = DataReader()
cleaner = DataCleaner()
transformer = DataTransformer()
saver = DataSaver()

# Read data from a CSV file
df = reader.read_csv('data/input.csv')

# Clean the data
cleaned_df = cleaner.clean_data(df)

# Transform the data
transformed_df = transformer.transform_data(cleaned_df)

# Save the transformed data to a new CSV file
saver.save_csv(transformed_df, 'data/output.csv')
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.