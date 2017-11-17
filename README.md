# San11SC
San11 Scenario Creator 

The tool helps to create San11 Scenario for multi-players. Each player chooses one city as capital and some heros to fight with others.

# Usage
### 1. Install Python (>=3.5)
### 2. Prepare game configure-file
The configure file is microsoft .xlsx file. (.xls is not support). Create a sheet named 'source' and configure on this sheet.

The sheet looks like the table below. The first line is the kings of each kingdom. The second line is the capital of each kingdom. The third and after lines are heros each player chosed.
<table class="table table-bordered table-striped table-condensed">  
    <tr>  
      <td>刘备</td>
      <td>曹操</td>
      <td>孙权</td>
      <td>...</td>
    </tr>  
    <tr>  
      <td>小沛</td>  
      <td>许昌</td>
      <td>柴桑</td>
      <td>...</td>
    </tr>
    <tr>
  <td>关羽</td>
  <td>郭嘉</td>
  <td>周瑜</td>
  <td>...</td>
    </tr>
        <tr>
  <td>张飞</td>
  <td>许褚</td>
  <td>陆逊</td>
  <td>...</td>
    </tr>
            <tr>
  <td>...</td>
  <td>...</td>
  <td>...</td>
  <td>...</td>
    </tr>
</table>  

### 3. Run the tool
```bash
$ chmod a+x exportMan.py
$ ./exportMan.py n m configure-file-name
```
> **n** is the number of players.  **m** is the number of heros for each player.
