echo "new commit"
read -p "name commit" commitname
git add .
git commit -m $commitname
git push
