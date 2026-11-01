---
records:
    - id: EXFB1SNYPD
      kind: monograph
      title: 'Probability-1: Volume 1'
      creators:
        - name: Albert N. Shiryaev
          role: author
      date: "2016"
      msc:
        - code: 60-01
          from: zbmath_search
        - code: 60Axx
          from: zbmath_search
        - code: 60Bxx
          from: zbmath_search
        - code: 60Fxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2016"
          ids:
            doi: 10.1007/978-0-387-72206-1
            zbl: "1390.60002"
            zbl_id: "5185747"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2016"
              ids:
                isbn:
                    - "9780387722054"
                    - "9780387722061"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-72206-1
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "5185747"
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
