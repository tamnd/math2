---
records:
    - id: MJWKKP4NF1
      kind: monograph
      title: Information and Coding Theory
      creators:
        - name: Gareth A. Jones
          role: author
        - name: J. Mary Jones
          role: author
      date: "2000"
      msc:
        - code: 68P30
          from: zbmath_search
        - code: 68-01
          from: zbmath_search
        - code: 94-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2000"
          ids:
            doi: 10.1007/978-1-4471-0361-5
            zbl: "0956.68052"
            zbl_id: "1493057"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2000"
              ids:
                isbn:
                    - "9781852336226"
                    - "9781447103615"
              access:
                class: record
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4471-0361-5
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "1493057"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: MJWNGM4S01
      kind: preprint
      title: On filtration formula and nodal sets in min-max theory
      creators:
        - name: Talant Talipov
          role: author
      date: "2026-09-29"
      msc:
        - code: 53-XX
          from: arxiv
        - code: 35-XX
          from: arxiv
        - code: 47-XX
          from: arxiv
        - code: 58-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.DG
        - system: arxiv
          code: math.AP
        - system: arxiv
          code: math.SP
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-09-29"
          ids:
            arxiv: "2609.37769"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.37769"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2609.37769"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
