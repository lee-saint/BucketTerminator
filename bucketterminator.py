import boto3

if __name__ == '__main__':
    client = boto3.client('s3')
    s3 = boto3.resource('s3')

    # 지우고 싶은 버킷에 들어 있는 문자열을 입력받는다
    bucket_name_substring = input('Bucket name you want to find: ')

    buckets = client.list_buckets()['Buckets']
    bucket_names_to_delete = [bks['Name'] for bks in buckets if bucket_name_substring in bks['Name']]

    if len(bucket_names_to_delete):  # 해당하는 버킷이 있으면 출력하고 지울 건지 물어보기
        print('Buckets found:')
        for bucket_name in bucket_names_to_delete:
            print(bucket_name)
        yesno = input("Are you sure you would like to delete these buckets? (only 'yes' will delete the buckets): ")
        if yesno == 'yes':  # 정확히 'yes'를 입력해야 삭제됨
            print('Deleting buckets...')
            for bucket_name in bucket_names_to_delete:
                bucket = s3.Bucket(bucket_name)
                bucket.object_versions.delete()
                bucket.delete()
            print('All buckets deleted.')
        else:
            print('Deletion cancelled.')
    else:  # 없으면 취소됨
        print('No buckets found!')

    print('Quitting...')
