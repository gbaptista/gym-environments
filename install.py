import subprocess
import gym


def install(package_folder, enviroments):
    pip_version_with_folder = subprocess.run(['pip', '--version'],
                                             stdout=subprocess.PIPE).stdout

    gym_folder = str(pip_version_with_folder).split()[3].replace('/pip',
                                                                 '/gym/envs')

    gym_package_folder = gym_folder + '/' + package_folder

    subprocess.run(['rm', '-rf', gym_folder + '/' + package_folder])
    subprocess.run(['cp', '-R', package_folder, gym_folder])
    subprocess.run(['rm', gym_folder + '/' + package_folder + '/register.py'])
    subprocess.run(['rm', '-rf', gym_package_folder + '/tests'])
    subprocess.run(['rm', '-rf', gym_package_folder + '/__pycache__'])

    registration_code = open(package_folder + '/register.py',
                             'r').read().strip()

    import_to_replace = 'from gym.envs.registration import register'

    registration_code = "\n" + registration_code.replace(import_to_replace,
                                                         '').strip() + "\n"

    current_envs_file = gym_folder + '/__init__.py'

    current_envs_code = open(current_envs_file, 'r').read()

    current_envs_code = current_envs_code.replace(registration_code, '')

    current_envs_code += registration_code

    open(current_envs_file, 'w').write(current_envs_code)

    print('')
    print(package_folder + ' Installed!')
    print('')
    print('> ' + current_envs_file + ' updated.')
    print('> ' + gym_folder + '/' + package_folder)

    for enviroment in enviroments:
        print('>', gym.make(enviroment))

    print('')


install('gbaptista', ['MultiArmedBanditEnv-v0'])
