---
records:
    - id: 4ZP6VYZDQP
      kind: monograph
      title: Functional Analysis
      creators:
        - name: Kôsaku Yosida
          role: author
      date: "1978"
      msc:
        - code: 46-XX
          from: zbmath_search
        - code: 46-02
          from: zbmath_search
        - code: 47D03
          from: zbmath_search
        - code: 47-02
          from: zbmath_search
        - code: 47A35
          from: zbmath_search
        - code: 35Dxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          label: 5th edition
          language: en
          date: "1978"
          ids:
            doi: 10.1007/978-3-642-96439-8
            zbl: "0365.46001"
            zbl_id: "3569238"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1978"
              ids:
                isbn:
                    - "9783642964411"
                    - "9783642964398"
              access:
                class: record
      relations:
        - kind: part_of
          to: GQFCNY816R
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-96439-8
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3569238"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
