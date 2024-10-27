package com.ohgiraffers.apirequest.section01;

import com.ohgiraffers.apirequest.section01.dto.RequestDTO;
import com.ohgiraffers.apirequest.section01.dto.ResponseDTO;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

/*
 * Spring에서 외부 API 요청 및 처리
 *
 * 대표적인 라이브러리
 * - HttpClient
 * - RestTemplate
 * - WebClient
 * - OpenFeign
 *
 * 주의할 점
 */

@RestController
@RequestMapping("/translate")
@Slf4j
@RequiredArgsConstructor
public class TransactionController {

    private final RestTemplateService restTemplateService;
    private final WebClientService webClientService;

    @GetMapping("/test")
    public String test() {
        log.info("/test -> get 요청 들어옴");
        return "test success";
    }

    @PostMapping("/resttemplate")
    public ResponseDTO translateByRestTemplate(@RequestBody RequestDTO requestDTO) {

        log.info("번역[RestTemplate] Controller 요청 들어옴");
        log.info("text: {}, lang:{}", requestDTO.getText(), requestDTO.getLang());

        ResponseDTO result = restTemplateService.translateText(requestDTO);

        return result;
    }

    @PostMapping("/webclient")
    public ResponseDTO translateByWebClient(@RequestBody RequestDTO requestDTO) {

        log.info("번역[WebClient] Controller 요청 들어옴");
        log.info("text: {}, lang:{}", requestDTO.getText(), requestDTO.getLang());

        ResponseDTO result = webClientService.translateText(requestDTO);

        return result;
    }
}
