from datetime import datetime

def update_status(query_set, event_type):
	if event_type == '배달완료':
		query_set.update(
			is_delivered = True, 
			delivered_at = datetime.now(),
			status = '배달완료'
		)
		return {
			'result': '200',
			'result_text': '수정이 완료되었습니다.'
		}

	elif event_type == '주문취소':
		query_set.update(
			is_refund_requested = True, 
			refund_requested_at = datetime.now(),
			status = '주문취소'
		)
		return {
			'result': '200',
			'result_text': '수정이 완료되었습니다.'
		}

	elif event_type == '주문접수':
		query_set.update(
			is_accepted = True, 
			accepted_at = datetime.now(),
			status = '주문접수'
		)

		return {
			'result': '200',
			'result_text': '접수가 완료되었습니다.'
		}


	else:
		return {
			'result': '201',
			'result_text': '알수 없는 오류입니다. 다시시도 해주세요.'
		}