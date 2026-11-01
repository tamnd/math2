---
records:
    - id: SF981M63JT
      kind: monograph
      title: Distributions, Partial Differential Equations, and Harmonic Analysis
      creators:
        - name: Dorina Mitrea
          role: author
      date: "2013"
      msc:
        - code: 46-01
          from: zbmath_search
        - code: 46Fxx
          from: zbmath_search
        - code: 47F05
          from: zbmath_search
        - code: 35-01
          from: zbmath_search
        - code: 35A08
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2013"
          ids:
            doi:
                - 10.1007/978-1-4614-8208-6
                - 10.1007/978-3-030-03296-8
            zbl: "1308.46002"
            zbl_id: "6189112"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2013"
              ids:
                isbn:
                    - "9781461482079"
                    - "9781461482086"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2018"
              ids:
                isbn:
                    - "9783030032951"
                    - "9783030032968"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4614-8208-6
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-03296-8
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "6189112"
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
