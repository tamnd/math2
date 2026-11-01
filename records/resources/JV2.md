---
records:
    - id: JV2PV9J7JN
      kind: monograph
      title: 'Geometric Methods and Applications: For Computer Science and Engineering'
      creators:
        - name: Jean Gallier
          role: author
      date: "2001"
      msc:
        - code: 53-01
          from: zbmath_search
        - code: 22-01
          from: zbmath_search
        - code: 51-01
          from: zbmath_search
        - code: 65D18
          from: zbmath_search
        - code: 51N10
          from: zbmath_search
        - code: 51N15
          from: zbmath_search
        - code: 51N20
          from: zbmath_search
        - code: 53A04
          from: zbmath_search
        - code: 53A05
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2001"
          ids:
            doi:
                - 10.1007/978-1-4419-9961-0
                - 10.1007/978-1-4613-0137-0
            zbl: "1031.53001"
            zbl_id: "1544763"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2011"
              ids:
                isbn:
                    - "9781441999603"
                    - "9781441999610"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2001"
              ids:
                isbn:
                    - "9781461265092"
                    - "9781461301370"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7B8JKAVW9F
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-9961-0
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4613-0137-0
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "1544763"
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
