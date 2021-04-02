import React from 'react'
import {
  CDropdown,
  CDropdownItem,
  CDropdownMenu,
  CDropdownToggle,
  CBadge
} from '@coreui/react'
import { freeSet } from '@coreui/icons'
import { flagSet } from '@coreui/icons'
import CIcon from '@coreui/icons-react'

import { useTranslation } from 'react-i18next'


const LanguageSwitcher = (props) => {
  const { i18n } = useTranslation()

  const languages = [
    {code: 'en', name: 'English', flag: flagSet.cifGb},
    {code: 'ru', name: 'Русский', flag: flagSet.cifRu},
    {code: 'ua', name: 'Українська', flag: flagSet.cifUa}
  ]

  const dropdownItems = languages.map((language) =>
    <CDropdownItem
      key={language.code}
      active={language.code === i18n.language}
      onClick={() => i18n.changeLanguage(language.code)}
    >
      <CIcon content={language.flag} className='mr-2' size="xl" />
      {language.name}
    </CDropdownItem>
  )

  return (
    <CDropdown
      inNav
      className="c-header-nav-item mx-2"
    >
      <CDropdownToggle className='c-header-nav-link' caret={false}>
        <CIcon content={freeSet.cilLanguage}/>
        <CBadge shape='pill' color='danger'>
          {i18n.language.toUpperCase()}
        </CBadge>
      </CDropdownToggle>
      <CDropdownMenu>
        {dropdownItems}
      </CDropdownMenu>
    </CDropdown>
  )
}

export default LanguageSwitcher