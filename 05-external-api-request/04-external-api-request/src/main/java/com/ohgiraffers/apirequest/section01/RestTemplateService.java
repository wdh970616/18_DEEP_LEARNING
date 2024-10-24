package com.ohgiraffers.apirequest.section01;

import com.ohgiraffers.apirequest.section01.dto.RequestDTO;
import com.ohgiraffers.apirequest.section01.dto.ResponseDTO;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClientException;
import org.springframework.web.client.RestTemplate;

/*
 * RestTemplate
 *
 * Spring에서 지원하는 객체로 간편하게 Rest방식 API를 호출할 수 있는 Spring의 내장 클래스
 * RESTAPI 서비스를 요청 후 응답받을 수 있게 설계되어 있음.
 *
 * 특징
 * - 간단하고 직관적인 사용법
 * - 동기식 처리로 이해하기 쉽다.
 */

@Service
@Slf4j
public class RestTemplateService {

    private final RestTemplate restTemplate;

    public RestTemplateService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    // 요청 보낼 URL
    private final String FAST_API_SERVER_URL = "http://localhost:8000/translate";

    public ResponseDTO translateText(RequestDTO requestDTO) {

        // HttpHeader
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        // requestBody
        // HttpEntity = header + body
        HttpEntity<RequestDTO> entity = new HttpEntity<>(requestDTO, headers);

        try {
            // 응답을 받을 타입
            ResponseEntity<ResponseDTO> response = restTemplate.exchange(
                    FAST_API_SERVER_URL, // 요청 URL
                    HttpMethod.POST,     // HTTP 메소드
                    entity,              // 요청 entity(헤더 + 본문)
                    ResponseDTO.class    // 응답을 받을 타입
            );

            log.info("=== 번역 서비스 응답 데이터 ===");
            log.info("번역 결과 : {}", response.getBody());

            return response.getBody();
        } catch (RestClientException e) {
            throw new RestClientException("");
        }
    }
}
