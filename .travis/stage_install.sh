
for script in \
    install_gym_environments.sh
do
    foldable source $TRAVIS_BUILD_DIR/.travis/$script
done
