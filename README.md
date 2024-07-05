# サーバーレスCI/CDパイプライン

このプロジェクトは、AWSサービスを使用してサーバーレスアーキテクチャを用いた継続的インテグレーションとデプロイメントのパイプラインを構築する方法を示します。

## 使用技術

- AWS CodePipeline
- AWS CodeBuild
- AWS Lambda
- Amazon S3


## セットアップ手順

1. リポジトリをクローンします:
    ```
    git clone <リポジトリURL>
    cd serverless-cicd-pipeline
    ```

2. S3バケットの作成:
    - ソースコードとビルド成果物を保存するためのS3バケットを作成します。

3. CodeBuildプロジェクトの作成:
    - AWS CodeBuildコンソールで新しいプロジェクトを作成し、`buildspec.yml`をビルド仕様として設定します。

4. Lambda関数のデプロイ:
    - `deploy_lambda.py`と`build_lambda.py`をそれぞれのLambda関数としてデプロイします。
    - 必要なIAMロールを設定して、各Lambda関数が適切な権限を持つようにします。

5. CodePipelineの設定:
    - `pipeline.yml`を使用してAWS CloudFormationを使い、CodePipelineを設定します。
    - パイプラインの各ステージで適切なリソースとアーティファクトを設定します。

6. パイプラインの実行:
    - ソースコードをS3バケットにアップロードし、パイプラインの実行を開始します。

## 使用方法

- ソースコードをS3にアップロードすると、CodePipelineが自動的にビルドとデプロイメントを実行します。
- CodeBuildがソースコードをビルドし、成果物をS3に保存します。
- Lambda関数が更新され、新しいコードがデプロイされます。




