sqlmap
Build Status Python 2.6|2.7|3.x License PyPI version GitHub closed issues Twitter

sqlmapはオープンソースのペネトレーションテスティングツールです。SQLインジェクションの脆弱性の検出、活用、そしてデータベースサーバ奪取のプロセスを自動化します。 強力な検出エンジン、ペネトレーションテスターのための多くのニッチ機能、持続的なデータベースのフィンガープリンティングから、データベースのデータ取得やアウトオブバンド接続を介したオペレーティング・システム上でのコマンド実行、ファイルシステムへのアクセスなどの広範囲に及ぶスイッチを提供します。

スクリーンショット
Screenshot

wikiに載っているいくつかの機能のデモをスクリーンショットで見ることができます。 スクリーンショット集

インストール
最新のtarballを こちら から、最新のzipballを こちら からダウンロードできます。

Git レポジトリをクローンして、sqlmapをダウンロードすることも可能です。:

git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
sqlmapは、 Python バージョン 2.6, 2.7 または 3.x がインストールされていれば、全てのプラットフォームですぐに使用できます。

使用法
基本的なオプションとスイッチの使用法をリストするには:

python sqlmap.py -h
全てのオプションとスイッチの使用法をリストするには:

python sqlmap.py -hh
実行例を こちら で見ることができます。 sqlmapの概要、機能の一覧、全てのオプションやスイッチの使用法を例とともに、 ユーザーマニュアル で確認することができます。

リンク
ホームページ: http://sqlmap.org
ダウンロード: .tar.gz or .zip
コミットのRSSフィード: https://github.com/sqlmapproject/sqlmap/commits/master.atom
課題管理: https://github.com/sqlmapproject/sqlmap/issues
ユーザーマニュアル: https://github.com/sqlmapproject/sqlmap/wiki
よくある質問 (FAQ): https://github.com/sqlmapproject/sqlmap/wiki/FAQ
Twitter: @sqlmap
デモ: http://www.youtube.com/user/inquisb/videos
スクリーンショット: https://github.com/sqlmapproject/sqlmap/wiki/Screenshots
