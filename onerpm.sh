#!/bin/bash

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#   Copyright (C) La Ode Muh. Fadlun Akbar

# temp_repo must be declared in the main script
# and assigned with specific directory
temp_repo="/tmp/onerpm"

# import function here
. /usr/share/onerpm/functions/cleanup
. /usr/share/onerpm/functions/check_package_corrupt
. /usr/share/onerpm/functions/check_location
. /usr/share/onerpm/functions/package_info
. /usr/share/onerpm/functions/install_process

see_package_info ()
{
  rm_temp
  local location=''
  local check_corrupt=''
  package_path_info location
  if [[ "$location" != '' ]]; then
    package_corrupt_status check_corrupt $location
    extract_package_info $location $check_corrupt
    print_package_info
    rm_temp
    local back
    while true; do
      read -p "Cari onerpm lain? [Y/n]: " back
      case "$back" in
        [Yy]|"" )
          see_package_info
          break
          ;;
        [Nn] )
          clear
          break
          ;;
      esac
    done
  fi
}

installation ()
{
  rm_temp
  local location=''
  local check_corrupt=''
  local user_confirm=''
  package_path_info location
  if [[ "$location" != '' ]]; then
    package_corrupt_status check_corrupt $location
    rm_temp
    install_confirm user_confirm
    extract_package_all $check_corrupt $location $user_confirm
    print_package_info
    install_process
    rm_temp
    ask_install_process_again installation
  fi
}

main ()
{
  echo "--------------------------------------"
  echo "-              ONERPM                -"
  echo "-      SINGE OFFLINE INSTALLER       -"
  echo "--------------------------------------"
  echo "-                                    -"
  echo "- 1. Install                         -"
  echo "- 2. Lihat Keterangan Suatu ONERPM   -"
  echo "- 3. Exit                            -"
  echo "-                                    -"
  echo -e "--------------------------------------\n"
  read -p "Pilihan [1-3]: " menu
  case "$menu" in
    1 )
      installation
      ;;
    2 )
      see_package_info
      ;;
    3 )
      rm_temp
      clear
      exit 0
      ;;
  esac
}

clear
while true; do
  main
done
