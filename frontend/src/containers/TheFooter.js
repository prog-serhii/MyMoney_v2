import React from 'react'
import { CFooter } from '@coreui/react'

const TheFooter = () => {
  return (
    <CFooter fixed={false}>
      <div>
        <a href="https://mymoney.ua" target="_blank" rel="noopener noreferrer">MyMoney</a>
        <span className="ml-1">&copy; 2020 Serhii Kazmiruk.</span>
      </div>
    </CFooter>
  )
}

export default React.memo(TheFooter)
